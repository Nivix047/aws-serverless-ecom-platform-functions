import os
import psycopg2
import json
from datetime import datetime
from dotenv import load_dotenv
import logging

# Load environment variables from .env file (for local development)
load_dotenv()

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))  # Log the incoming event

    # Retrieve environment variables for the RDS database connection
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    connection = None
    cursor = None

    try:
        # Establish a connection to the RDS instance
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

        # Convert rows into a list of dictionaries
        users = []
        for row in rows:
            user = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'comments': row[4],
                'created_at': row[5].isoformat() if isinstance(row[5], datetime) else row[5]  # Convert datetime to ISO format
            }
            users.append(user)

        # Return the result in a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps(users)  # Ensure the body is a JSON string
        }

    except Exception as e:
        # Log the error and return the error message
        logger.error("Error: %s", str(e))  # Log the error message
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})  # Return the error message as JSON
        }

    finally:
        # Close cursor and connection if they were created
        if cursor:
            cursor.close()
        if connection:
            connection.close()
