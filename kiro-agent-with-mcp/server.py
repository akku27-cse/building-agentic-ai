from mcp.server.fastmcp import FastMCP
from pymongo import MongoClient, errors

# ---------------- MongoDB connection ---------------- #
try:
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
    db = client["ai-agent-mcp"]
    users = db["user"]
    # Test connection
    client.admin.command("ping")
    print("MongoDB connected successfully")
except errors.ServerSelectionTimeoutError:
    print("Failed to connect to MongoDB")
    exit(1)

# ---------------- Initialize MCP server ---------------- #
mcp = FastMCP("mongo-agent")
print("Server running...")

# ---------------- TOOLS ---------------- #

@mcp.tool()
def add_user(user_id: str, name: str, role: str):
    users.insert_one({
        "_id": user_id,
        "name": name,
        "role": role
    })
    return f"User {name} added successfully"

@mcp.tool()
def delete_user(user_id: str):
    result = users.delete_one({"_id": user_id})
    return "User deleted successfully" if result.deleted_count else "User not found"

@mcp.tool()
def update_user_field(user_id: str, field: str, value: str):
    ALLOWED_FIELDS = ["name", "role"]
    if field not in ALLOWED_FIELDS:
        return "Field not allowed"
    result = users.update_one({"_id": user_id}, {"$set": {field: value}})
    return f"Updated {field} successfully" if result.matched_count else "User not found"

@mcp.tool()
def get_user(user_id: str):
    user = users.find_one({"_id": user_id}, {"_id": 0})
    return user if user else {"error": "User not found"}

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    mcp.run()
