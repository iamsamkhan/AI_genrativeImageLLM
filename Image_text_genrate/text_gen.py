import os
import openai
#import urllib.request
#from datetime import datetime

open.api_key=os.getenv("OPENAI.API_KEY") #

data=""

response=openai.Completion.create(
    prompt=data,
    engine="text-davinci-001",
    temperature=0.5,
    max_tokens=60,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0.0
)
