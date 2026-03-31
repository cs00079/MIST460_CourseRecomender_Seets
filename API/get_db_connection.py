import pyodbc

import pyodbc

def get_db_connection():
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=tcp:mist460-server-seets.database.windows.net,1433;"
        "DATABASE=MIST460_RDB_Seets;"
        "UID=APILogin;"
        "PWD=MI$T460Instructor;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    return pyodbc.connect(connection_string)