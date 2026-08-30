import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")
#od gory to jest ta czesc zeby nie wklejac na chama klucza anthropic

print(api_key[:15])  


{
  "model": "claude-sonnet-5",
  "max_tokens": 200,
  "messages": [
    {"role": "user", "content": "Cześć"}
  ]
}