class OpportunityScorer:

    def __init__(self):

        self.keywords = {
            "ai": 15,
            "openai": 20,
            "chatgpt": 20,
            "google": 10,
            "microsoft": 10,
            "nvidia": 15,
            "tesla": 12,
            "apple": 10,
            "amazon": 10,

            "business": 12,
            "startup": 15,
            "money": 12,
            "investment": 15,
            "finance": 12,

            "viral": 15,
            "breaking": 15,
            "trend": 10,
            "future": 10,

            "robot": 12,
            "technology": 10,
            "indonesia": 8,
        }

    def calculate(self, title):

        score = 50

        lower = title.lower()

        for word, value in self.keywords.items():

            if word in lower:
                score += value

        if len(title) < 40:
            score += 5

        if "?" in title:
            score += 3

        if score > 100:
            score = 100

        return score