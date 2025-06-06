import streamlit as st

st.set_page_config(page_title="Sneaker Scout Full Platform", layout="wide")
st.title("👟 Sneaker Scout | All-In-One Dashboard")

menu = st.sidebar.radio(
    "📍 Navigate",
    ["🏠 Dashboard Home", "🔎 Scout", "🎟️ Raffle Radar", "⏰ Timer", "📘 GuideBot", "📈 FlipIQ", "🔐 AccessCode"]
)

if menu == "🏠 Dashboard Home":
    st.header("🏠 Sneaker Scout Dashboard Home")
    st.markdown("Welcome to your command center for sneaker drop intelligence.")
    st.markdown("Choose a tool from the sidebar to get started.")
    st.image("https://cdn-icons-png.flaticon.com/512/861/861512.png", width=200)
    st.markdown("---")

if menu == "🔎 Scout":
    st.header("🔎 Scout – Sneaker Drop Scanner")
    st.image("https://cdn-icons-png.flaticon.com/512/2947/2947654.png", width=100)
    st.write("Scout monitors SNKRS, Foot Locker, Adidas Confirmed, and Shopify-based stores.")
    st.success("Real-time alerts are sent via Discord, SMS, or email.")

if menu == "🎟️ Raffle Radar":
    st.header("🎟️ Raffle Radar – Raffle Watcher")
    st.image("https://cdn-icons-png.flaticon.com/512/3771/3771381.png", width=100)
    st.write("Tracks open raffles by brand and region. Helps you enter in time.")
    st.warning("Pro Tip: Use multiple verified accounts for higher success.")

if menu == "⏰ Timer":
    st.header("⏰ Timer – Countdown Agent")
    st.image("https://cdn-icons-png.flaticon.com/512/1827/1827504.png", width=100)
    st.write("Keeps countdowns to all confirmed sneaker drops with clickable links.")
    st.info("Next drop: Air Jordan 1 OG – June 10, 10:00 AM EST")

if menu == "📘 GuideBot":
    st.header("📘 GuideBot – Sneaker Strategy Coach")
    st.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=100)
    st.write("Covers strategy tips for manual vs bot copping, proxies, and account farming.")
    st.success("You are learning from the best. Consistency = cops.")

if menu == "📈 FlipIQ":
    st.header("📈 FlipIQ – Resale Value Bot")
    st.image("https://cdn-icons-png.flaticon.com/512/3126/3126608.png", width=100)
    st.write("Estimates resale value using StockX, GOAT, and eBay data.")
    st.info("Today’s hot flip: Travis Scott Olive – Est. Profit $320")

if menu == "🔐 AccessCode":
    st.header("🔐 AccessCode – Member Gating Agent")
    st.image("https://cdn-icons-png.flaticon.com/512/942/942751.png", width=100)
    st.write("Controls access to features based on plan (Free, Basic, Pro, Lifetime).")
    st.warning("Upgrade to unlock weekly FlipIQ reports and raffle automation.")
