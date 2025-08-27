from dotenv import load_dotenv

load_dotenv()

from providers import openai
# from providers import anthropic
# from providers import xai
# from providers import google
# from providers import groq
# from providers import ollama

openai.main()
# openai.book_finder()
# openai.image_reader()

# anthropic.main()
# xai.main()
# google.main()
# groq.main()
# ollama.main()
