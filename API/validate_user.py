from get_db_connection import get_db_connection
import pymssql

def validate_user(username: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)

    cursor.execute("EXEC procValidateUser %s, %s", (username, password))

    try:
        rows = cursor.fetchall()
    except pymssql.Error:
        rows = []

    conn.close()

    results = [dict(row) for row in rows]
    return {"data": results}