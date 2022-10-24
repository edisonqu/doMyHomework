import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="7. Provide a work related example of Machiavellianism",
  temperature=0.7,
  max_tokens=2599,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
print(response["choices"][0]["text"])