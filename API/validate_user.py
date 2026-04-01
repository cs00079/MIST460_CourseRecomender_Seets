from API.get_db_connection import get_db_connection

def validate_user(username: str, password: str,):
  
  
  
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("{CALL dbo.procValidateUser(?, ?)}", (username, bytes.fromhex(password.replace("0x",""))))
    rows = cursor.fetchall()
    conn.close()

    results = [
        {
            "AppUserID": row.AppUserID,
            "Fullname": row.Fullname,
        }
        for row in rows
    ]

    return {"data": results}
