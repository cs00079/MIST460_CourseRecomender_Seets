from datetime import datetime
from langchain_openai import OpenAIEmbeddings
from get_db_connection import get_db_connection
import json
import pprint
from find_current_semester import find_current_semester
from format_context import format_context
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def get_course_recommendations_for_selected_job(job_description: str) -> str:

    year_value = datetime.now().year
    semester_value = find_current_semester()
    user_query = f"Based on the following job description, recommend relevant courses from our database offered in {semester_value} {year_value}: {job_description}"

    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    job_description_embedding = embedding_model.embed_query(job_description)

    pprint.pprint(job_description_embedding)

    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)

    cursor.execute("EXEC procGetCourseRecommendationsForSelectedJob %s, %s, %s", 
                   (json.dumps(job_description_embedding), semester_value, year_value))
    
    semantically_similar_courses = cursor.fetchall()
    course_count = len(semantically_similar_courses)
    semantic_results_for_context = format_context(semantically_similar_courses)

    cursor.close()
    conn.close()

    pprint.pprint(semantic_results_for_context)

    generative_model = ChatOpenAI(model="gpt-4o", temperature=0)

    prompt = ChatPromptTemplate.from_messages([
    (
        "system",
                    """
                    You are an expert academic advisor helping students identify courses 
                    that align with a target job description.

                    You will be given:
                    - A user query describing a job or career goal
                    - A set of retrieved course records, each with a title, description, 
                    and a cosine distance score (lower = better match)

                    Your task:
                    1. For each retrieved course, assess whether it genuinely prepares a 
                    student for the stated job role based solely on the course description.
                    2. If a course is a strong match, explain specifically which skills or 
                    topics in the description align with the job requirements.
                    3. Be honest about weak matches rather than forcing a justification.
                    4. Rank the courses from most to least relevant in your response.
                    5. Do not invent course content, prerequisites, or outcomes not stated 
                    in the provided descriptions.
                    6. If none of the retrieved courses are a good fit, say so clearly and 
                    suggest the student speak with an advisor directly.
                    """
    ),
    (
        "human",
                    """
                    User Query:
                    {user_query}

                    Retrieved Courses ({course_count} results, ranked by relevance):
                    {context}

                    Please provide your course recommendations, ranked from best to worst fit.
                    Cite the match score and specific evidence from each description to justify 
                    your reasoning. Flag any course with a distance score above 0.4 as a weak match.
                    """
        )
    ])

    chain = prompt | generative_model
    response = chain.invoke({
        "user_query": user_query,
        "context": semantic_results_for_context,
        "course_count": course_count
    })
    return response