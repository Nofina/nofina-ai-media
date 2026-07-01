from .analyzer import OpportunityAnalyzer
from .trend import TrendAnalyzer
from .strategy import StrategyPlanner
from .monetizer import Monetizer


class NofinaBrain:

    def __init__(self):

        self.analyzer = OpportunityAnalyzer()
        self.trend = TrendAnalyzer()
        self.strategy = StrategyPlanner()
        self.monetizer = Monetizer()

    def analyze(self, article):

        result = self.analyzer.analyze(article)

        trend = self.trend.analyze(article)

        strategy = self.strategy.analyze(result)

        monetizer = self.monetizer.analyze(result)

        result.update(trend)
        result.update(strategy)
        result.update(monetizer)

        return result

    def analyze_all(self, articles):

        results = []

        for article in articles:
            results.append(
                self.analyze(article)
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results