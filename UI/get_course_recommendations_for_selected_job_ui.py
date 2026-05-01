import streamlit as st
from fetch_data import fetch_data, fetch_text

def get_job_title(record):
    return record['JobTitle']

def get_course_recommendations_for_selected_job_ui():
    st.title("Course Recommendations for Selected Job")

    df = fetch_data("get_all_jobs/", {})

    if df is None or df.empty:
        st.error("Could not load jobs. Please try again later.")
        return

    selected_job = st.selectbox(
        "Select a job",
        options=df.to_dict(orient="records"),
        format_func=get_job_title,
    )

    st.markdown(f"### You selected: **{selected_job['JobTitle']}**")

    job_description = st.text_area(
        "Job description (feel free to edit)",
        value=selected_job['JobDescription'],
        height=200,
    )

    if st.button("Get Course Recommendations"):
        with st.spinner("Generating recommendations... please wait 10-20 seconds"):
            response = fetch_text(
                "get_course_recommendations_for_selected_job/",
                {"job_description": job_description},
            )
        if response:
            content = response.get("content", "")
            st.subheader("Recommended Courses")
            st.markdown(content, unsafe_allow_html=True)
        else:
            st.info("No recommendations found for the selected job. Try another one!")