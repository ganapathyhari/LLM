import os

os.environ["OLLAMA_API_KEY"] = "5a009cdb1a8a47daa5d8040de75ba02e.wUb5rQXusJZhdZ7LpxCAewnT"

import ollama
response = ollama.web_search("What is the capital of France?")
print(response)
