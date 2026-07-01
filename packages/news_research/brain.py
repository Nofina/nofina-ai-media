class NofinaBrain:

    def analyze(self, article):

        title = article["title"].lower()

        result = {}

        # Opportunity Score
        score = 50

        keywords = {
            "ai":15,
            "chatgpt":20,
            "openai":20,
            "google":10,
            "microsoft":10,
            "nvidia":15,
            "tesla":12,
            "business":10,
            "money":10,
            "startup":12,
            "viral":15,
            "indonesia":8,
            "robot":10,
        }

        for k,v in keywords.items():
            if k in title:
                score += v

        score=min(score,100)

        result["score"]=score

        # Virality
        result["virality"]=min(score+5,100)

        # Revenue
        if score>=85:
            revenue="High"
        elif score>=70:
            revenue="Medium"
        else:
            revenue="Low"

        result["revenue"]=revenue

        # Competition
        if score>=90:
            competition="High"
        elif score>=70:
            competition="Medium"
        else:
            competition="Low"

        result["competition"]=competition

        # Evergreen
        evergreen=60

        if "ai" in title:
            evergreen=90

        if "business" in title:
            evergreen=85

        result["evergreen"]=evergreen

        # Audience

        audience=[]

        if "ai" in title:
            audience.append("AI Enthusiast")

        if "business" in title:
            audience.append("Entrepreneur")

        if "indonesia" in title:
            audience.append("Indonesia Audience")

        if audience==[]:
            audience=["General Audience"]

        result["audience"]=audience

        # Platform

        if score>=85:
            platform=[
                "YouTube Shorts",
                "TikTok",
                "Instagram Reels",
                "Facebook Reels"
            ]
        else:
            platform=[
                "Facebook",
                "Threads"
            ]

        result["platform"]=platform

        # Video Duration

        if score>=80:
            duration="45-60 Seconds"
        else:
            duration="30 Seconds"

        result["duration"]=duration

        # Priority

        if score>=90:
            stars="★★★★★"
        elif score>=80:
            stars="★★★★"
        elif score>=70:
            stars="★★★"
        else:
            stars="★★"

        result["priority"]=stars

        return result