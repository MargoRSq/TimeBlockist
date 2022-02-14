from starlette.config import Config
from todoist_api_python.api import TodoistAPI

env = Config(".env")

TOKEN = env('TOKEN')

api = TodoistAPI(TOKEN)

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
