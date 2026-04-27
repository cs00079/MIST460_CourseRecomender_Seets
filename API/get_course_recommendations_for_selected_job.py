from datetime import datetime
from langchain_openai import OpenAIEmbeddings
import pprint

def get_course_recommendations_for_selected_job(job_description: str) -> str:
    
    year_value = 2026
    semester_value = "Spring"
    user_query = f"Based on the following job description, recommend relevant courses from our database offered in spring{year_value}: {job_description}"

    #Use the openAI embeddings model to create an embedding for the job description
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

    job_description_embedding = embedding_model.enbed_query(job_description)

    print("\nJob Description Embedding")
    pprint.pprint(job_description_embedding)

if __name__ == "_main_":
    sample_job_description = "Agentic"