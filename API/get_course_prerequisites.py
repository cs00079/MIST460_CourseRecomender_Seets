from API.get_db_connection import get_db_connection

def get_course_prerequisites(
    subject_code: str = None,
    course_number: str = None
):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("{CALL dbo.procGetCoursePrerequisites(?, ?)}", (subject_code, course_number))
    rows = cursor.fetchall()
    conn.close()
    
    results = [
        {
            "Title": row.Title,
            "SubjectCode": row.SubjectCode,
            "CourseNumber": row.CourseNumber,
            "MinGradeRequired": row.MinGradeRequired
        }
        for row in rows
    ]

    return {"data": results}