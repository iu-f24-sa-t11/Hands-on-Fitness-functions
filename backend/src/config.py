import os

APP_ROOT_PATH = "/api"

DB_HOST = "mongodb://mongodb:27017"
DB_NAME = "ApplicationDatabase"

DOMAIN = os.getenv("DOMAIN", default="localhost")
DELETE_CODE = os.getenv("DELETE_CODE", default=None)
DROP_CODE = os.getenv("DROP_CODE", default=None)
