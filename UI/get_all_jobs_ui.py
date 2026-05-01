import streamlit as st
from fetch_data import fetch_data

def get_job_title(record):
    return record["JobTitle"]

def get_course_recommendations_for_selected_job_ui():
    st.title("Course Reccomendations for Selected Job")

    df = fetch_data("get_all_jobs/", params={})
    
    #Build a dropdown to select a job
    
    selected_job = st.selectbox("Select a Job", 
                                options=df.to_dict(orient="records"),
                                format_func=get_job_title)
    st.write(f"You selected: {get_job_title(selected_job)}")
    parameters = {}
    
    parameters["job_description"] = st.text_area("Job Description", value=selected_job["Job"])

