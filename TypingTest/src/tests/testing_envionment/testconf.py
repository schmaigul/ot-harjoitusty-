import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", "..", "..", ".env.test"))
except FileNotFoundError:
    print('Environment file not found')

TEST_USER_DATABASE_FILENAME = os.getenv("TEST_USER_DATABASE_FILENAME") or "test_users.sqlite"
TEST_USER_DATABASE_PATH = os.path.join(dirname, "..", "..", "..", "data", TEST_USER_DATABASE_FILENAME)

TEST_STATISTIC_DATABASE_FILENAME = os.getenv("TEST_STATISTIC_DATABASE_FILENAME") or "test_statistics.sqlite"
TEST_STATISTICS_DATABASE_PATH = os.path.join(dirname, "..", "..", "..", "data", TEST_STATISTIC_DATABASE_FILENAME)
