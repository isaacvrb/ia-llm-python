import os
import openai
from pydantic import BaseModel

openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class BookResponse(BaseModel):
  title: str
  author: str

def book_finder():
  book_description = input("Descreva um livro: ")

  response = openai_client.chat.completions.parse(
    model="gpt-5-nano",
    messages=[
      {
        "role": "system",
        "content": "Você é um guia de livros muito experiente."
      },
      {
        "role": "user",
        "content": f"Me dê as informações com a seguinte característica: {book_description}. Priorize o título em português, se existir."
      }
    ],
    response_format=BookResponse
  )

  message = response.choices[0].message

  if message.parsed:
    print(f"Livro: {message.parsed.title}")
    print(f"Autor: {message.parsed.author}")
  else:
    print("Livro não encontrado")
  
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
  
  output_text = response.input_text
  
  print(output_text)
  return output_text


