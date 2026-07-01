class TrendAnalyzer:

    def analyze(self, article):

        title = article["title"].lower()

        trend_score = 50
        reasons = []

        keywords = {
            "openai": 20,
            "chatgpt": 20,
            "gpt": 18,
            "ai": 15,
            "google": 10,
            "microsoft": 10,
            "tesla": 10,
            "nvidia": 15,
            "viral": 20,
            "breaking": 15,
            "startup": 10,
            "business": 10,
        }

        for keyword, value in keywords.items():
            if keyword in title:
                trend_score += value
                reasons.append(f"Contains keyword '{keyword}'")

        trend_score = min(trend_score, 100)

        if trend_score >= 90:
            level = "Very High"
        elif trend_score >= 75:
            level = "High"
        elif trend_score >= 60:
            level = "Medium"
        else:
            level = "Low"

        return {
            "trend_score": trend_score,
            "trend_level": level,
            "trend_reason": reasons
        }