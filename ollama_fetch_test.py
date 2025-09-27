import os

os.environ["OLLAMA_API_KEY"] = ""

import ollama
response = ollama.web_search("What is the capital of France?")
print(response)
