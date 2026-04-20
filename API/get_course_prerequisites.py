from get_db_connection import get_db_connection
import pymssql

def get_course_prerequisites(
    subject_code: str = None,
    course_number: str = None,
):
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)
    #cursor.execute("{CALL procGetCoursePrerequisites(?, ?)}", (subject_code, course_number))
    cursor.execute("EXEC procGetCoursePrerequisites %s, %s", (subject_code, course_number))
    
    try:
        rows = cursor.fetchall()
    except pymssql.Error:
        rows = []

    conn.close()

    #Convert rows to list of dictionaries

    results = [dict(row) for row in rows]

    return {"data": results}