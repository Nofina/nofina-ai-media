class Monetizer:

    def analyze(self, article):

        score = article["score"]

        if score >= 90:
            revenue = "Very High"
            rpm = "$12 - $20"
            affiliate = True
            sponsor = True

        elif score >= 75:
            revenue = "High"
            rpm = "$8 - $12"
            affiliate = True
            sponsor = False

        elif score >= 60:
            revenue = "Medium"
            rpm = "$4 - $8"
            affiliate = False
            sponsor = False

        else:
            revenue = "Low"
            rpm = "$1 - $4"
            affiliate = False
            sponsor = False

        return {
            "revenue_level": revenue,
            "estimated_rpm": rpm,
            "affiliate": affiliate,
            "sponsor_friendly": sponsor,
        }