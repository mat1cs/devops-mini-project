import psycopg2
import time
from psycopg2 import OperationalError

class Database:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self, retries=5, delay=2):
        for attempt in range(retries):
            try:
                print(f"Attempt {attempt + 1} to connect to the database...")
                self.connection = psycopg2.connect(
                    host=self.config.db_host,
                    user=self.config.db_user,
                    password=self.config.db_password,
                    dbname=self.config.db_name
                )
                print("Database connection established.")
                return
            except OperationalError as e:
                print(f"Connection failed: {e}")
                time.sleep(delay)
        raise Exception("Could not connect to the database after multiple attempts.")

    def create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL
                );
            """)
            self.connection.commit()
    
    def insert_message(self, content):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO messages (content) VALUES (%s)",
                (content,)
            )
            self.connection.commit()
    
    def get_messages(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT id, content FROM messages;")
            return cursor.fetchall()