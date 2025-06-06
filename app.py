import streamlit as st

st.set_page_config(page_title="Sneaker Scout Agents", layout="centered")
st.title("👟 Sneaker Scout Agent Lineup")

agents = [
    {
        "name": "Scout",
        "role": "Sneaker Drop Scanner",
        "description": "Monitors major sites like SNKRS, Foot Locker, Adidas Confirmed, and Shopify. Sends real-time alerts via Discord, SMS, or Email."
    },
    {
        "name": "Raffle Radar",
        "role": "Raffle Watcher",
        "description": "Tracks upcoming raffles by region, brand, and date. Sends reminders with links to enter early and often."
    },
    {
        "name": "Timer",
        "role": "Drop Countdown Agent",
        "description": "Maintains an updated calendar of upcoming drops with times, launch methods (FCFS, raffle, draw), and clickable links."
    },
    {
        "name": "GuideBot",
        "role": "Sneaker Strategy Coach",
        "description": "Educates users on best practices for manual and bot-based cop methods, including proxy setup, account farming, and drop preparation."
    },
    {
        "name": "FlipIQ",
        "role": "Resale Value Projection Bot",
        "description": "Scrapes StockX, GOAT, and eBay for estimated profits. Delivers ROI insights and resale heat rankings."
    },
    {
        "name": "AccessCode",
        "role": "Member Gating Agent",
        "description": "Manages tiered access to alerts, strategy content, and dashboard tools based on user’s membership level."
    }
]

for agent in agents:
    st.subheader(f"🤖 {agent['name']} – {agent['role']}")
    st.write(agent['description'])
    st.markdown("---")


st.set_page_config(page_title="Sneaker Scout Dashboard", layout="wide")
st.title("🏠 Sneaker Scout Dashboard Home")

st.markdown("Welcome to your command center for sneaker drop intelligence. Choose a tool below:")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2947/2947654.png", width=80)
    if st.button("🔎 Scout - Drop Alerts"):
        st.write("Redirecting to Drop Scanner...")

    st.image("https://cdn-icons-png.flaticon.com/512/3771/3771381.png", width=80)
    if st.button("🎟️ Raffle Radar"):
        st.write("Redirecting to Raffle Tracker...")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/1827/1827504.png", width=80)
    if st.button("⏰ Timer - Countdown"):
        st.write("Redirecting to Drop Countdown...")

    st.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=80)
    if st.button("📘 GuideBot - Strategy"):
        st.write("Redirecting to Sneaker Strategy Guide...")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/3126/3126608.png", width=80)
    if st.button("📈 FlipIQ - Resale Intel"):
        st.write("Redirecting to Resale Value Reports...")

    st.image("https://cdn-icons-png.flaticon.com/512/942/942751.png", width=80)
    if st.button("🔐 AccessCode - Membership"):
        st.write("Redirecting to Membership Controls...")

st.markdown("---")
st.info("Pro Tip: Bookmark this page to quickly jump to your Sneaker Scout tools.")
