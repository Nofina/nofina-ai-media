from packages.ai.content_ai import ContentAI

ai = ContentAI()

opportunity = {
    "title": "OpenAI launches GPT-6",
    "score": 90,
    "category": "AI",
    "trend_level": "Very High",
    "revenue_level": "Very High",
    "main_platform": "YouTube Shorts",
}

result = ai.generate(opportunity)

print(result)