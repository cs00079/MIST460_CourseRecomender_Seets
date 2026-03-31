from typing import Optional
from fastapi import FastAPI


from API.get_course_sections_for_specified_course import get_course_sections_for_specified_course
from API.get_course_prerequisites import get_course_prerequisites

# Create FastAPI app
app = FastAPI()

# This endpoint returns all available sections for a given course
@app.get("/get_course_sections_for_specified_course/")

def get_course_sections_for_specified_course_endpoint(
    subject_code: Optional[str] = None,
    course_number: Optional[str] = None
):
    return get_course_sections_for_specified_course(subject_code, course_number)

# This endpoint returns prerequisites for a given course
@app.get("/get_course_prerequisites/")

def get_course_prerequisites_endpoint(
    subject_code: Optional[str] = None,
    course_number: Optional[str] = None
):
    return get_course_prerequisites(subject_code, course_number)
