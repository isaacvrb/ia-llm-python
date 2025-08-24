import os
import openai

openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
  response = openai_client.responses.create(
    model="gpt-5-nano",
    reasoning={
      "effort": "low"
    },
    input=[
      {
        "role": "system",
        "content": [
          {
            "type": "input_text",
            "text": "Seja direto e conciso, uma única frase como resposta."
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": input("Digite uma pergunta: ")
          }
        ]
      }
    ]
  )
  
  print(response.output_text)
  return response.output_text


