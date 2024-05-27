import os
from sqlalchemy import create_engine

def main():
    db_user = os.getenv('CONNECTIFY_MYSQL_USER')
    db_pwd = os.getenv('CONNECTIFY_MYSQL_PWD')
    db_host = os.getenv('CONNECTIFY_MYSQL_HOST')
    db_name = os.getenv('CONNECTIFY_MYSQL_DB')

    if not all([db_user, db_pwd, db_host, db_name]):
        print("Please set all required environment variables.")
        return

    engine_url = f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}'
    try:
        engine = create_engine(engine_url)
        connection = engine.connect()
        print("Connected to the database successfully.")
        connection.close()
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    main()
