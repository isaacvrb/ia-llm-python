import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
  response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=genai.types.GenerateContentConfig(
      system_instruction="Seja direto e conciso, uma única frase como resposta."
    ),
    contents=input("Digite uma pergunta: "),
  )
  text = response.text
  
  print(text)
  return text