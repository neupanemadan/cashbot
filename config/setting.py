import os
from dotenv import load_dotenv

# Load env var from dotenv file
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
env_path = os.path.join(APP_ROOT, '.env')
load_dotenv(env_path)

API_KEY = os.getenv('API_KEY')
