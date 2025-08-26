import os
import ollama

def main():
  # response = ollama.generate(
  #   model="llama3.1",
  #   prompt=input("Digite uma pergunta: "),
  #   system="Seja direto e conciso, uma única frase como resposta."
  # )

  response = ollama.chat(
    model="llama3.1",
    messages=[
      {
        "role": "system",
        "content": "Seja direto e conciso, uma única frase como resposta."
      },
      {
        "role": "user",
        "content": input("Digite uma pergunta: ")
      }
    ]
  )
  
  text = response["message"]["content"]
  
  print(text)
  return text