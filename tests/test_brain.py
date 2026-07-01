from packages.brain.brain import NofinaBrain

brain = NofinaBrain()

article = {
    "title": "OpenAI launches GPT-6",
    "source": "Reuters",
    "link": "https://example.com"
}

result = brain.analyze(article)

print(result)
