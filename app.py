import os
import psycopg2
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Custom JSON encoder to handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO format string
        return json.JSONEncoder.default(self, obj)

def lambda_handler(event, context):
    # Retrieve environment variables for the RDS database connection
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    connection = None
    cursor = None

    # Establish a connection to the RDS instance
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()

        # Perform a simple query (e.g., fetching all users)
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        # Return the result in a JSON response using the custom encoder for datetime
        return {
            'statusCode': 200,
            'body': json.dumps(rows, cls=DateTimeEncoder)
        }

    except Exception as e:
        # Log the error and return the error message
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }

    finally:
        # Close cursor and connection if they were created
        if cursor:
            cursor.close()
        if connection:
            connection.close()
