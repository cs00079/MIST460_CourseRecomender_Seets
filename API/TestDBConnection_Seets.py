from pathlib import Path
from get_db_connection import get_db_connection
import os
import pyodbc
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
print(f"Using env file: {env_path}")

load_dotenv(dotenv_path=env_path)


def test_db_connection():

    required_vars = [
        "DB_SERVER",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
        "DB_DRIVER"
    ]

    missing = [v for v in required_vars if not os.getenv(v)]

    assert not missing, f"Missing env vars: {missing}"
    print("✅ Env vars loaded")

    conn = get_db_connection()
    assert isinstance(conn, pyodbc.Connection), "Expected a pyodbc.Connection"
    print("✅ Connection object returned")

    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    assert result is not None, "Query returned no results"
    assert result[0] == 1, "Expected query result of 1"
    print("✅ Connection is live and queryable")

    conn.close()
    print("✅ Connection closed cleanly")
    print("\n🎉 All tests passed!")


if __name__ == "__main__":
    test_db_connection()