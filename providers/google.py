import os
import google.generativeai as gai

gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
  return True