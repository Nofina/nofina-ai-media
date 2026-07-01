import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[2]

sys.path.append(str(ROOT))

from packages.brain.brain import NofinaBrain
from packages.news_research.content_generator import generate_content
from packages.news_research.parser import load_articles

st.set_page_config(
    page_title="Nofina AI Media",
    page_icon="🧠",
    layout="wide"
)

brain = NofinaBrain()

st.title("🧠 NOFINA AI MEDIA")
st.caption("AI Opportunity Intelligence Dashboard")

articles = load_articles()

if not articles:
    st.warning("Belum ada berita. Jalankan news_agent.py dulu.")
    st.stop()

opportunities = brain.analyze_all(articles)

top_score = opportunities[0]["score"] if opportunities else 0
high_count = len([x for x in opportunities if x["score"] >= 85])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Opportunities", len(opportunities))
col2.metric("Top Score", top_score)
col3.metric("High Opportunities", high_count)
col4.metric("Engine Status", "Running")

st.divider()
st.subheader("🔥 Top Opportunities Today")

for index, item in enumerate(opportunities):
    with st.container(border=True):
        st.markdown(f"### {item['title']}")
        st.caption(f"{item['source']} | Category: {item['category']}")

        a, b, c, d = st.columns(4)

        a.metric("Opportunity Score", item["score"])
        b.metric("Trend", item["trend_level"])
        c.metric("Revenue", item["revenue_level"])
        d.metric("RPM", item["estimated_rpm"])

        st.write(f"🎬 **Main Platform:** {item['main_platform']}")
        st.write(f"⏱ **Duration:** {item['duration']}")
        st.write(f"🧲 **Hook:** {item['hook']}")
        st.write(f"📱 **Platforms:** {', '.join(item['platform'])}")
        st.write(f"🤝 **Affiliate:** {'✅ Yes' if item['affiliate'] else '❌ No'}")
        st.write(f"🎯 **Sponsor Friendly:** {'✅ Yes' if item['sponsor_friendly'] else '❌ No'}")

        with st.expander("📈 Trend Reason"):
            for reason in item["trend_reason"]:
                st.write(f"- {reason}")

        st.link_button("📖 Read Article", item["link"])

        if st.button("🚀 Generate Content Package", key=f"gen_{index}"):
            package = generate_content(item)

            st.success("Content generated")

            st.markdown("#### 🎬 YouTube Title")
            st.write(package["youtube_title"])

            st.markdown("#### 🪝 Hook")
            st.write(package["hook"])

            st.markdown("#### 📝 Script")
            st.text_area("Script", package["script"], height=260)

            st.markdown("#### 🖼 Thumbnail Prompt")
            st.text_area("Thumbnail Prompt", package["thumbnail_prompt"], height=180)

            st.markdown("#### # Hashtags")
            st.write(package["hashtags"])