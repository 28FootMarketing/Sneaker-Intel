import streamlit as st
import datetime
import time
import random

st.set_page_config(page_title="Sneaker Scout: Live + Scraper", layout="wide")
st.title("📡 Sneaker Scout | Streaming, Interactive, + Live Drop Feed")

menu = st.sidebar.radio(
    "📍 Navigate",
    ["🏠 Home", "🔎 Scout", "🎟️ Raffle Radar", "⏰ Timer (Live)", "📘 GuideBot", "📈 FlipIQ", "🔐 AccessCode", "📡 Live Feed"]
)

if menu == "🏠 Home":
    st.header("🏠 Dashboard Overview")
    st.markdown("This version includes real-time countdowns, strategy tools, AND dynamic drop scraping.")
    st.info("Navigate using the sidebar.")

if menu == "🔎 Scout":
    st.header("🔎 Scout – Sneaker Drop Scanner")
    keyword = st.text_input("Track Sneaker Keyword")
    if keyword:
        st.success(f"Now tracking for keyword: {keyword}")

if menu == "🎟️ Raffle Radar":
    st.header("🎟️ Raffle Radar – Get Alerted")
    brand = st.selectbox("Brand", ["Nike", "Adidas", "New Balance"])
    email = st.text_input("Enter Email for Raffle Alerts")
    if st.button("Save Reminder"):
        st.success(f"{brand} raffle alerts will be sent to {email}")

if menu == "⏰ Timer (Live)":
    st.header("⏰ Countdown – Jordan 1 OG")
    drop_time = datetime.datetime(2025, 6, 10, 10, 0, 0)
    placeholder = st.empty()
    while True:
        now = datetime.datetime.now()
        delta = drop_time - now
        if delta.total_seconds() <= 0:
            placeholder.success("🚨 DROP IS LIVE!")
            break
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        placeholder.info(f"Drop in: {hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)

if menu == "📘 GuideBot":
    st.header("📘 Strategy Coach")
    topic = st.selectbox("Pick Topic", ["Manual Copping", "Using Bots", "Proxy Setup", "Account Farming"])
    tips = {
        "Manual Copping": "Use autofill. Be signed in. Refresh 10s before.",
        "Using Bots": "Schedule tasks 2 minutes early with rotating proxies.",
        "Proxy Setup": "Use residential IPs. Avoid reused data center proxies.",
        "Account Farming": "Create and warm multiple accounts weekly."
    }
    st.success(tips[topic])

if menu == "📈 FlipIQ":
    st.header("📈 FlipIQ – Resale Estimator")
    shoe = st.selectbox("Select Sneaker", ["Travis Scott Olive", "Jordan 4 Thunder", "Yeezy Slide Bone"])
    resale = {
        "Travis Scott Olive": "$320 🔥🔥🔥",
        "Jordan 4 Thunder": "$180 🔥🔥",
        "Yeezy Slide Bone": "$70 🔥"
    }
    st.info(f"Expected Profit: {resale[shoe]}")

if menu == "🔐 AccessCode":
    st.header("🔐 Membership Plan")
    plan = st.radio("Choose Plan", ["Free", "Basic", "Pro", "Lifetime"])
    access = {
        "Free": "1 alert/week, no resale tips.",
        "Basic": "Full alerts + raffles.",
        "Pro": "All features unlocked.",
        "Lifetime": "Permanent access to everything."
    }
    st.success(access[plan])

if menu == "📡 Live Feed":
    st.header("📡 Live Sneaker Drop Feed (Simulated Scrape)")
    st.markdown("This section simulates live scraping of drop data every time you click refresh.")

    if st.button("🔁 Refresh Data"):
        drops = [
            {"model": "Jordan 1 High OG UNC", "date": "June 14", "site": "SNKRS", "resale": "$210"},
            {"model": "Yeezy Boost 350 Pirate Black", "date": "June 16", "site": "Adidas Confirmed", "resale": "$400"},
            {"model": "Nike SB Dunk Low 'Panda Pigeon'", "date": "June 12", "site": "Skate Shops", "resale": "$250"},
            {"model": "New Balance 550 Rich Paul", "date": "June 18", "site": "New Balance", "resale": "$180"}
        ]
        selected = random.sample(drops, 3)
        for drop in selected:
            st.markdown(f"**Model:** {drop['model']}  
**Date:** {drop['date']}  
**Site:** {drop['site']}  
**Est. Resale:** {drop['resale']}")
            st.markdown("---")
    else:
        st.warning("Click the button above to simulate live drop scraping.")
