import streamlit as st

# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="Rating | Royal Spice Hotel",
    page_icon="⭐",
    layout="wide"
)

# ==============================
# PAGE STYLE
# ==============================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff4e6, #f5dfc5);
}

.rating-title {
    text-align: center;
    color: #5a2d18;
    font-size: 48px;
    font-weight: 800;
    margin-top: 30px;
}

.rating-subtitle {
    text-align: center;
    color: #8b5e3c;
    font-size: 20px;
    margin-bottom: 45px;
}

.rating-card {
    background: #fffaf3;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid #d6ad85;
    box-shadow: 0 8px 20px rgba(80, 45, 20, 0.12);
}

.big-rating {
    text-align: center;
    font-size: 55px;
    font-weight: 800;
    color: #a0522d;
}

.footer {
    text-align: center;
    margin-top: 60px;
    color: #8b5e3c;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="rating-title">⭐ Rate Your Experience</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="rating-subtitle">'
    'Your feedback helps Royal Spice Hotel serve you better ❤️'
    '</div>',
    unsafe_allow_html=True
)

# ==============================
# CURRENT RATING
# ==============================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="rating-card">'
        '<div class="big-rating">4.8 ⭐</div>'
        '<p style="text-align:center;">Customer Rating</p>'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="rating-card">'
        '<div class="big-rating">6 🍽️</div>'
        '<p style="text-align:center;">Menu Items</p>'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="rating-card">'
        '<div class="big-rating">❤️</div>'
        '<p style="text-align:center;">Happy Customers</p>'
        '</div>',
        unsafe_allow_html=True
    )

# ==============================
# RATING FORM
# ==============================

st.divider()

st.markdown("## ⭐ Give Your Rating")

rating = st.slider(
    "How would you rate your experience?",
    min_value=1,
    max_value=5,
    value=5
)

st.write(
    f"Your Rating: {'⭐' * rating}"
)

food = st.selectbox(
    "🍽️ What did you enjoy?",
    [
        "Masala Dosa",
        "Idli",
        "Uttappa",
        "Uggani Bajji",
        "Coffee",
        "Green Tea"
    ]
)

feedback = st.text_area(
    "💬 Your Feedback",
    placeholder="Tell us about your experience..."
)

# ==============================
# SUBMIT
# ==============================

if st.button(
    "⭐ Submit Rating",
    use_container_width=True
):

    st.success(
        f"Thank you for rating {food}! ❤️"
    )

    st.balloons()

# ==============================
# FOOTER
# ==============================

st.markdown(
    '<div class="footer">'
    '🌶️ <b>Royal Spice Hotel</b><br>'
    'Fresh • Tasty • Smart ❤️<br>'
    '<small>Thank you for visiting us!</small>'
    '</div>',
    unsafe_allow_html=True
)