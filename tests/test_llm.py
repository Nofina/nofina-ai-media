from packages.llm.client import ask_ai

response = ask_ai(
    "Perkenalkan dirimu dalam 3 kalimat. Jawab dalam bahasa Indonesia."
)

print(response)