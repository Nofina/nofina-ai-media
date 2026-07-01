class NofinaBrain:

    def analyze(self, article):

        title = article["title"].lower()

        result = {}

        # -----------------------------
        # Viral Score
        # -----------------------------

        viral = 50

        keywords = {

            "ai":20,
            "chatgpt":20,
            "openai":20,
            "google":12,
            "tesla":15,
            "nvidia":18,
            "startup":12,
            "robot":15,
            "indonesia":8,
            "business":10,
            "money":12,
            "crypto":15,
            "bitcoin":15,
            "iphone":10,
            "apple":10

        }

        for word,value in keywords.items():

            if word in title:

                viral += value

        viral=min(viral,100)

        result["viral_score"]=viral

        # -----------------------------

        if viral>=90:

            result["revenue"]="Very High"

        elif viral>=80:

            result["revenue"]="High"

        elif viral>=65:

            result["revenue"]="Medium"

        else:

            result["revenue"]="Low"

        # -----------------------------

        if viral>=85:

            result["competition"]="High"

        elif viral>=70:

            result["competition"]="Medium"

        else:

            result["competition"]="Low"

        # -----------------------------

        evergreen=True

        if any(x in title for x in ["today","breaking","live","yesterday"]):

            evergreen=False

        result["evergreen"]=evergreen

        # -----------------------------

        if "ai" in title or "chatgpt" in title:

            audience="Technology"

        elif "business" in title:

            audience="Entrepreneur"

        elif "money" in title:

            audience="Finance"

        else:

            audience="General"

        result["audience"]=audience

        # -----------------------------

        if viral>=85:

            result["platform"]="YouTube Shorts + TikTok + Facebook Reels"

        elif viral>=70:

            result["platform"]="YouTube Shorts"

        else:

            result["platform"]="Facebook"

        # -----------------------------

        if audience=="Technology":

            angle="Future Technology"

        elif audience=="Entrepreneur":

            angle="Business Opportunity"

        elif audience=="Finance":

            angle="Money"

        else:

            angle="General News"

        result["angle"]=angle

        # -----------------------------

        if viral>=85:

            idea="Video + Blog + Newsletter"

        elif viral>=70:

            idea="Video Shorts"

        else:

            idea="Facebook Post"

        result["monetization"]=idea

        return result