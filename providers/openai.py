import os
import openai

openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test():
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
            "text": "Qual o sentido da vida?"
          }
        ]
      }
    ]
  )
  
  return response


