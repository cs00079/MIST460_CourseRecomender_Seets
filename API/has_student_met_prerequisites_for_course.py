from get_db_connection import get_db_connection

def has_student_met_prerequisites_for_course(
    student_id: int,
    subject_code: str,
    course_number: str,
):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("{CALL dbo.procHasStudentMetPrerequisitesForCourse(?, ?, ?)}", (student_id, subject_code, course_number))
    rows = cursor.fetchall()
    conn.close()

    results = [
        {
            "SubjectCode": row[0],
            "CourseNumber": row[1],
            "MinimumGradeRequired": row[2],
        }
        for row in rows
    ]

    return {"data": results}