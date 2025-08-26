import os
import groq

groq_client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

def main():
  response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
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

  message = response.choices[0].message.content

  print(message)
  return message