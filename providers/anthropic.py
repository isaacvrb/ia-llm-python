import os
import anthropic

anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def main():
  response = anthropic_client.messages.create(
    model="claude-sonnet-4-20250514",
    system="Seja direto e conciso, uma única frase como resposta.",
    max_tokens=1024,
    messages=[
      {
        "role": "user",
        "content": input("Digite uma pergunta: ")
      }
    ],
  )

  message = response.content[0].text

  print(message)
  return message