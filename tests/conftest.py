import pytest
import snowflake.connector
from config import SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT, SNOWFLAKE_WAREHOUSE, SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA

@pytest.fixture(scope="session")
def db_connection():
    conn = snowflake.connector.connect(
        user='Testuser',
        password='Snowtest5*',
        account='sjrdkku-gp34174',
        warehouse='COMPUTE_WH',
        database='Customer_Onboarding',
        schema='Customer_Onboarding'
    )
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()
