import os
import openai
import urllib.request
from datetime import datetime
open.api_key=os.getenv("OPENAI_API_KEY")
user_prompt=input("write promat for DALL -E2:")

response=openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024*1024"
)

image_url=response["data"][0]["url"]
print("mage_url")