import streamlit as st

# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="Welcome | Royal Spice Hotel",
    page_icon="🌶️",
    layout="wide"
)

# ==============================
# PREMIUM STYLE
# ==============================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff8ef,
        #f3dfc7,
        #fff4e6
    );
}

.welcome {
    text-align: center;
    padding: 55px 20px 35px;
}

.small-title {
    font-size: 18px;
    letter-spacing: 7px;
    color: #9a6846;
    font-weight: 700;
}

.hotel-title {
    font-size: 58px;
    font-weight: 900;
    color: #542914;
    margin: 12px 0;
}

.tagline {
    font-size: 25px;
    color: #8a4724;
    font-weight: 600;
}

.description {
    font-size: 18px;
    color: #76513b;
    margin-top: 15px;
}

.section-title {
    text-align: center;
    color: #542914;
    font-size: 32px;
    font-weight: 800;
    margin: 35px 0 8px;
}

.section-text {
    text-align: center;
    color: #80604a;
    font-size: 17px;
    margin-bottom: 25px;
}

.food-card {
    background: #fffaf4;
    padding: 18px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #d8b28d;
    box-shadow: 0 10px 25px rgba(80,45,20,0.13);
}

.food-name {
    color: #5a2d18;
    font-size: 22px;
    font-weight: 800;
}

.food-description {
    color: #795548;
    font-size: 14px;
    margin-top: 6px;
}

.info-card {
    background: rgba(255,250,243,0.92);
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #d6ad85;
    box-shadow: 0 8px 22px rgba(80,45,20,0.12);
}

.info-card h3 {
    color: #5a2d18;
    font-size: 21px;
}

.info-card p {
    color: #795548;
}

.footer {
    text-align: center;
    margin-top: 60px;
    padding: 25px;
    color: #8b5e3c;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# WELCOME
# ==============================

st.markdown(
    '<div class="welcome">'
    '<div class="small-title">WELCOME TO</div>'
    '<div class="hotel-title">🌶️ ROYAL SPICE HOTEL</div>'
    '<div class="tagline">Where Tradition Meets Taste ❤️</div>'
    '<div class="description">'
    'Authentic South Indian flavours, freshly prepared with love.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ==============================
# HERO IMAGE
# ==============================

st.image(
    "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?auto=format&fit=crop&w=1600&q=90",
    use_container_width=True
)


# ==============================
# SPECIALITIES
# ==============================

st.markdown(
    '<div class="section-title">🍽️ Our South Indian Specialities</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-text">'
    'Traditional flavours prepared fresh for you every day ❤️'
    '</div>',
    unsafe_allow_html=True
)


# ==============================
# FOOD 1
# ==============================

col1, col2 = st.columns(2)

with col1:

    st.image(
        "https://images.unsplash.com/photo-1630383249896-424e482df921?auto=format&fit=crop&w=900&q=90",
        use_container_width=True
    )

    st.markdown(
        '<div class="food-card">'
        '<div class="food-name">🥞 Masala Dosa</div>'
        '<div class="food-description">'
        'Crispy golden dosa filled with delicious traditional masala.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with col2:

    st.image(
        "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=900&q=90",
        use_container_width=True
    )

    st.markdown(
        '<div class="food-card">'
        '<div class="food-name">🥣 South Indian Breakfast</div>'
        '<div class="food-description">'
        'A delicious combination of fresh and traditional favourites.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ==============================
# FOOD 2
# ==============================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.image(
        "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=900&q=90",
        use_container_width=True
    )

    st.markdown(
        '<div class="food-card">'
        '<div class="food-name">🍽️ Uttappa</div>'
        '<div class="food-description">'
        'Soft, tasty and freshly prepared with delicious toppings.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with col2:

    st.image(
        "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=900&q=90",
        use_container_width=True
    )

    st.markdown(
        '<div class="food-card">'
        '<div class="food-name">☕ Traditional Coffee</div>'
        '<div class="food-description">'
        'A refreshing cup of coffee to complete your South Indian meal.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ==============================
# EXPERIENCE
# ==============================

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="info-card">'
        '<h3>🍽️ Fresh Tiffins</h3>'
        '<p>Freshly prepared South Indian favourites every morning.</p>'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="info-card">'
        '<h3>🤖 AI Food Assistant</h3>'
        '<p>Smart recommendations based on your food preferences.</p>'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="info-card">'
        '<h3>❤️ Royal Experience</h3>'
        '<p>A simple, modern and enjoyable ordering experience.</p>'
        '</div>',
        unsafe_allow_html=True
    )


# ==============================
# FOOTER
# ==============================

st.markdown(
    '<div class="footer">'
    '🌶️ <b>ROYAL SPICE HOTEL</b><br>'
    'Fresh • Traditional • Smart ❤️<br>'
    '<small>AI-Based Online Food Ordering System</small>'
    '</div>',
    unsafe_allow_html=True
)