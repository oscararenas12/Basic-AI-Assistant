import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # This will automatically look for .env in the parent directory

# Now you can access your environment variables
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# These are already set in your .env file, so we don't need to set them again
# But we can verify they're set correctly:
print(f"LANGCHAIN_TRACING_V2: {os.getenv('LANGCHAIN_TRACING_V2')}")
print(f"LANGCHAIN_PROJECT: {os.getenv('LANGCHAIN_PROJECT')}")

# You can now use these variables in your code
print(f"Azure Endpoint: {azure_endpoint}")
print(f"LangChain API Key: {langchain_api_key}")
# Don't print the full API key for security reasons
print(f"Azure API Key: {azure_api_key[:5]}...{azure_api_key[-5:]}")