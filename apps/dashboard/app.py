import sys
from pathlib import Path

import streamlit as st

# Root Project
ROOT = Path(__file__).resolve().parents[2]

# Tambahkan path packages
sys.path.append(str(ROOT / "packages" / "brain"))
sys.path.append(str(ROOT / "packages" / "generators"))
sys.path.append(str(ROOT / "packages" / "news-research"))

from brain import NofinaBrain
from content_generator import generate_content

st.set_page_config(
    page_title="Nofina AI Media",
    page_icon="🧠",
    layout="wide"
)

brain = NofinaBrain()

NEWS_FILE = ROOT / "packages" / "news-research" / "outputs" / "latest_news.txt"

st.title("🧠 NOFINA AI MEDIA")
st.caption("AI Opportunity Intelligence Dashboard")