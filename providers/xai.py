import os
import xai_sdk
from xai_sdk.chat import system, user, assistant

xai_client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

def main():
  chat = xai_client.chat.create(model="grok-3-mini")
  chat.append(system("Seja direto e conciso, uma única frase como resposta."))
  chat.append(user("Qual o significado do amor?"))

  response = chat.sample()
  content = response.content
  
  print(content)
  return content