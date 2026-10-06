import streamlit as st

st.set_page_config(
    page_title="About | Royal Spice Hotel",
    page_icon="🌶️",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff4e6, #f5dfc5);
}

.about-title {
    text-align: center;
    color: #5a2d18;
    font-size: 48px;
    font-weight: 800;
    margin-top: 30px;
}

.about-subtitle {
    text-align: center;
    color: #8b5e3c;
    font-size: 20px;
    margin-bottom: 40px;
}

.about-card {
    background: #fffaf3;
    padding: 35px;
    border-radius: 22px;
    border: 1px solid #d6ad85;
    box-shadow: 0 8px 20px rgba(80, 45, 20, 0.12);
    margin-bottom: 25px;
}

.about-heading {
    color: #7a3f21;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 15px;
}

.about-card p {
    color: #6f4a35;
    font-size: 17px;
    line-height: 1.8;
}

.highlight {
    color: #8b451f;
    font-weight: 700;
}

.footer {
    text-align: center;
    margin-top: 60px;
    color: #8b5e3c;
    padding-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="about-title">🌶️ About Royal Spice Hotel</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="about-subtitle">'
    'Where tradition, taste and technology come together ❤️'
    '</div>',
    unsafe_allow_html=True
)


# ==============================
# OUR STORY
# ==============================

st.markdown("""
<div class="about-card">

<div class="about-heading">
🏨 Our Story
</div>

<p>
Royal Spice Hotel was created with a simple idea —
to bring the authentic taste of South Indian food to
customers through a warm, fresh and enjoyable dining
experience.
</p>

<p>
Our concept is inspired by the traditional South Indian
breakfast culture, where every morning begins with the
aroma of freshly prepared <span class="highlight">dosa, idli,
uttappa and a refreshing cup of coffee.</span>
</p>

<p>
At Royal Spice Hotel, we believe that great food is not
only about taste. It is also about <span class="highlight">
fresh ingredients, quality preparation, cleanliness and
customer happiness.</span>
</p>

<p>
Our menu brings together delicious South Indian tiffins
and refreshing drinks, prepared with care to give
customers a simple yet satisfying food experience.
</p>

<p>
Along with traditional flavours, Royal Spice Hotel also
embraces modern technology. Our <span class="highlight">
AI-Based Online Food Ordering System</span> makes it
easier for customers to explore the menu, place orders
and discover food based on their preferences.
</p>

<p>
❤️ <b>Our goal is simple:</b> serve fresh and tasty food,
provide a comfortable experience and make every visit
to Royal Spice Hotel memorable.
</p>

</div>
""", unsafe_allow_html=True)


# ==============================
# OUR MISSION
# ==============================

st.markdown("""
<div class="about-card">

<div class="about-heading">
❤️ Our Mission
</div>

<p>
Our mission is to provide tasty, fresh and affordable
South Indian food while making the ordering experience
simple, fast and enjoyable.
</p>

<p>
We aim to combine traditional food values with modern
technology so that customers can enjoy both great taste
and a convenient digital ordering experience.
</p>

</div>
""", unsafe_allow_html=True)


# ==============================
# AI FEATURE
# ==============================

st.markdown("""
<div class="about-card">

<div class="about-heading">
🤖 Smart AI Experience
</div>

<p>
Our AI Food Assistant recommends dishes based on the
customer's preferences, helping customers quickly
discover something they may enjoy.
</p>

<p>
This smart feature makes the ordering process more
personalized and demonstrates how Artificial Intelligence
can be used to improve everyday food services.
</p>

</div>
""", unsafe_allow_html=True)


# ==============================
# HIGHLIGHTS
# ==============================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🍽️ Menu Items", "6")

with col2:
    st.metric("⭐ Customer Rating", "4.8 / 5")

with col3:
    st.metric("⏰ Open Hours", "7 AM - 10 PM")


# ==============================
# FOOTER
# ==============================

st.markdown(
    """
    <div class="footer">
        🌶️ <b>Royal Spice Hotel</b><br>
        Fresh • Tasty • Smart ❤️<br>
        <small>AI-Based Online Food Ordering System</small>
    </div>
    """,
    unsafe_allow_html=True
)