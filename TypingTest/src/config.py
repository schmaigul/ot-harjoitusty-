import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    print('Environment file not found')

USER_DATABASE_FILENAME = os.getenv("USER_DATABASE_FILENAME") or "users.sqlite"
USER_DATABASE_PATH = os.path.join(dirname, "..", "data", USER_DATABASE_FILENAME)

STATISTIC_DATABASE_FILENAME = os.getenv("STATISTIC_DATABASE_FILENAME") or "statistics.sqlite"
STATISTICS_DATABASE_PATH = os.path.join(dirname, "..", "data", STATISTIC_DATABASE_FILENAME)
