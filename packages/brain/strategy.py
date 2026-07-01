class StrategyPlanner:

    def analyze(self, article):

        score = article["score"]

        if score >= 90:
            duration = "45-60 Seconds"
            hook = "Berita ini bisa mengubah industri!"
            content = "Short Video"
            platform = "YouTube Shorts"

        elif score >= 75:
            duration = "30-45 Seconds"
            hook = "Topik ini sedang ramai dibahas."
            content = "Short Video"
            platform = "TikTok"

        else:
            duration = "30 Seconds"
            hook = "Mari kita bahas berita ini."
            content = "Facebook Post"
            platform = "Facebook"

        return {
            "duration": duration,
            "hook": hook,
            "recommended_content": content,
            "main_platform": platform
        }