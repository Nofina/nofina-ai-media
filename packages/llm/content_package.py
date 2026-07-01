import json

from packages.llm.client import ask_ai
from packages.llm.prompts import CONTENT_PROMPT


def generate_content_package(news):

    prompt = f"""
{CONTENT_PROMPT}

Berita:

Title:
{news["title"]}

Source:
{news["source"]}

Link:
{news["link"]}
"""

    response = ask_ai(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "title": news["title"],
            "hook": "",
            "script": response,
            "caption": "",
            "hashtags": [],
            "thumbnail_text": "",
            "thumbnail_prompt": "",
            "voice_style": "",
            "broll_keywords": [],
            "cta": ""
        }