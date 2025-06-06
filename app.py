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
