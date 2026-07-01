def generate_content(article):

    title = article["title"]

    youtube_title = f"🔥 {title}"

    hook = f"Berita ini sedang ramai dibicarakan. {title}"

    script = f"""
HOOK:
{hook}

ISI:

Hari ini ada perkembangan menarik.

{title}

Berita ini sedang menjadi perhatian banyak orang dan diperkirakan akan terus berkembang.

Bagaimana menurut kalian?

Follow untuk update berita AI setiap hari.
"""

    thumbnail = f"""
Create a cinematic YouTube Shorts thumbnail.

Headline:
{title}

Style:
Modern, dramatic lighting, ultra realistic, high contrast, viral thumbnail.
"""

    hashtags = "#AI #Technology #News #Shorts"

    return {
        "youtube_title": youtube_title,
        "hook": hook,
        "script": script,
        "thumbnail_prompt": thumbnail,
        "hashtags": hashtags,
    }