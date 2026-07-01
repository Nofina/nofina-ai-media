from .scorer import OpportunityScorer


class OpportunityAnalyzer:

    def __init__(self):
        self.scorer = OpportunityScorer()

    def analyze(self, article):

        title = article["title"]

        score = self.scorer.calculate(title)

        category = self.detect_category(title)

        revenue = self.revenue(score)

        platform = self.platform(score)

        content_type = self.content_type(score)

        return {
            "title": title,
            "source": article["source"],
            "link": article["link"],
            "score": score,
            "category": category,
            "revenue": revenue,
            "platform": platform,
            "content_type": content_type,
        }

    def detect_category(self, title):

        lower = title.lower()

        if any(x in lower for x in ["ai", "openai", "chatgpt", "robot"]):
            return "AI"

        if any(x in lower for x in ["business", "startup", "money"]):
            return "Business"

        if any(x in lower for x in ["google", "apple", "tesla", "microsoft", "amazon"]):
            return "Big Tech"

        if "indonesia" in lower:
            return "Indonesia"

        return "General"

    def revenue(self, score):

        if score >= 85:
            return "High"

        if score >= 70:
            return "Medium"

        return "Low"

    def platform(self, score):

        if score >= 85:
            return [
                "YouTube Shorts",
                "TikTok",
                "Instagram Reels",
                "Facebook Reels",
            ]

        if score >= 70:
            return [
                "YouTube Shorts",
                "Facebook Reels",
            ]

        return [
            "Facebook",
            "Threads",
        ]

    def content_type(self, score):

        if score >= 85:
            return "Short Video"

        if score >= 70:
            return "Educational Short"

        return "Social Post"