# backend/core/database.py

import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

# These come from your .env file
MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_DB_NAME = os.environ.get("MONGODB_DB_NAME", "academic_notifier")

# We create one client instance shared across the entire app
# Creating a new connection on every request would be very slow
client = AsyncIOMotorClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]

# These are our "collections" — think of them like tables in SQL
notices_collection = db["notices"]
users_collection = db["users"]