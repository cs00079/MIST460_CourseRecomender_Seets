from get_db_connection import get_db_connection


def get_course_sections_for_specified_course(subject_code, course_number):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT *
        FROM Section
        WHERE SubjectCode = ? AND CourseNumber = ?
    """

    cursor.execute(query, subject_code, course_number)

    rows = cursor.fetchall()

    conn.close()

    return [tuple(row) for row in rows]