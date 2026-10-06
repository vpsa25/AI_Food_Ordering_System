import streamlit as st

st.set_page_config(
    page_title="Home | Royal Spice Hotel",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #f8f1e7,
        #ead2b7,
        #f7eadb
    );
}

.home-title {
    text-align: center;
    color: #4a2c1d;
    font-size: 48px;
    font-weight: 900;
    margin-top: 35px;
}

.home-subtitle {
    text-align: center;
    color: #795548;
    font-size: 19px;
    margin-bottom: 40px;
}

.home-card {
    background: rgba(255,255,255,0.75);
    padding: 30px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #c9a27e;
    box-shadow: 0 8px 22px rgba(78,52,37,0.12);
}

.card-title {
    color: #5a3825;
    font-size: 22px;
    font-weight: 800;
}

.card-text {
    color: #795548;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="home-title">🏠 Welcome to Royal Spice Hotel</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="home-subtitle">Traditional South Indian Taste • Freshly Prepared • Smart Ordering</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="home-card">
        <div class="card-title">🍽️ Delicious Tiffins</div>
        <div class="card-text">
            Enjoy freshly prepared South Indian favourites every day.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="home-card">
        <div class="card-title">🤖 AI Food Assistant</div>
        <div class="card-text">
            Get smart food recommendations based on your preferences.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="home-card">
        <div class="card-title">❤️ Royal Experience</div>
        <div class="card-text">
            Simple ordering with a premium hotel experience.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="home-title" style="font-size:32px;">✨ Today at Royal Spice</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🍽️ Menu Items", "6")

with col2:
    st.metric("⭐ Customer Rating", "4.8 / 5")

with col3:
    st.metric("🕘 Open Hours", "7 AM – 10 PM")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
text-align:center;
color:#6b4226;
font-size:15px;
padding:20px;
">
🌶️ <b>Royal Spice Hotel</b><br>
Fresh • Traditional • Smart
</div>
""", unsafe_allow_html=True)