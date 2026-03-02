import os

class Config:
    def __init__(self):
        self.app_env = os.getenv('APP_ENV', 'development')
        self.app_port = int(os.getenv('APP_PORT', 5000))

        self.db_host = os.getenv('DB_HOST', 'localhost')
        self.db_user = os.getenv('DB_USER', 'user')
        self.db_password = os.getenv('DB_PASSWORD', 'password')
        self.db_name = os.getenv('DB_NAME', 'app_db')

if __name__ == "__main__":
    config = Config()
    print("APP_ENV:", config.app_env)
    print("APP_PORT:", config.app_port)
    print("DB_HOST:", config.db_host)
    print("DB_USER:", config.db_user)
    print("DB_PASSWORD:", config.db_password)
    print("DB_NAME:", config.db_name)