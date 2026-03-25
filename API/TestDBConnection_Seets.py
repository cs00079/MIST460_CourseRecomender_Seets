from get_db_connection import get_db_connection

import os

import pyodbc

from dotenv import load_dotenv

load_dotenv()

def test_db_connection():

    # Test 1: check env vars are loaded

    required_vars = ['DB_SERVER', 'DB_NAME', 'DB_USER', 'DB_PASSWORD']
    
    missing = [v for v in required_vars if v not in os.environ(v)]

    assert not missing, f'Missing env vars: {missing}'

    assert not missing, f"Missing env vars: {missing}"

    print("✅ Env vars loaded")


    # Test 2: Connection returns a pyopdbc. Connection object

    conn = get_dbconnection()

    assert isinstance(conn, pyodbc.Connection), "Expected pyodbc.Connection"

    print("✅ Connection object returned")

    