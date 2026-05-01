import streamlit as st
import requests

API_URL = "https://mist460-api-seets.azurewebsites.net/get_course_recommendations_for_selected_job/"

def get_course_recommendations_for_selected_job_ui():
    st.title("Course Recommendations for a Job")
    st.write("Paste a job description to get relevant courses from the catalog.")

    job_description = st.text_area(
        "Job Description",
        height=220,
        placeholder="e.g. Data analyst requiring SQL, Python, and data visualization skills."
    )

    if st.button("Recommend Courses"):
        if not job_description or not job_description.strip():
            st.warning("Please enter a job description.")
        else:
            try:
                with st.spinner("Getting course recommendations..."):
                    response = requests.get(
                        API_URL,
                        params={"job_description": job_description},
                        timeout=120
                    )
                if response.status_code == 200:
                    st.success("Recommendations received!")
                    st.write(response.json())
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to API: {str(e)}")