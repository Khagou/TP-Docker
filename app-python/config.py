import os

config = {
    'user' : os.getenv("DB_USER"),
    'password' : os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT")),
    'database': os.getenv("DB_NAME")
}