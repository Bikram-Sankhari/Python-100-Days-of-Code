import os
from dotenv import load_dotenv

load_dotenv("secret.env")

print(os.getenv("name"))
