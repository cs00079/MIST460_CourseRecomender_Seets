import streamlit as st
from get_course_sections_for_specified_course_ui import get_course_sections_for_specified_course_ui
from get_course_prerequisites_ui import get_course_prerequisites_ui
from validate_user_ui import validate_user_ui
from has_student_met_prerequisites_for_course_ui import has_student_met_prerequisites_for_course_ui
from get_course_recommendations_for_selected_job_ui import get_course_recommendations_for_selected_job_ui

if "app_user_id" not in st.session_state:
    st.session_state.app_user_id = None

with st.sidebar:
    st.title("Course Recommender System")

    api_end_point = st.selectbox(
        "Select a course recommendation functionality:",
        [
            "Validate User",
            "Get Course Sections for Specified Course",
            "Get Course Prerequisites",
            "Has Student Met Prerequisites for Course",
            "Get Course Recommendations for Selected Job"
        ]
    )

if api_end_point == "Get Course Sections for Specified Course":
    get_course_sections_for_specified_course_ui()
elif api_end_point == "Get Course Prerequisites":
    get_course_prerequisites_ui()
elif api_end_point == "Validate User":
    validate_user_ui()
elif api_end_point == "Has Student Met Prerequisites for Course":
    if st.session_state.app_user_id is None:
        st.warning("Please validate user first.")
        validate_user_ui()
    else:
        has_student_met_prerequisites_for_course_ui()
elif api_end_point == "Get Course Recommendations for Selected Job":
    get_course_recommendations_for_selected_job_ui()