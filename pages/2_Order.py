import streamlit as st

# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="Order | Royal Spice Hotel",
    page_icon="🍽️",
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

.order-title {
    text-align: center;
    color: #5a2d18;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

.order-subtitle {
    text-align: center;
    color: #8b5e3c;
    font-size: 20px;
    margin-bottom: 40px;
}

.food-card {
    background: #fffaf3;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #d6ad85;
    box-shadow: 0 8px 20px rgba(80, 45, 20, 0.12);
    margin-bottom: 20px;
}

.food-name {
    color: #5a2d18;
    font-size: 24px;
    font-weight: 700;
}

.price {
    color: #a0522d;
    font-size: 22px;
    font-weight: 700;
}

.cart-box {
    background: #fffaf3;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #d6ad85;
    box-shadow: 0 8px 20px rgba(80, 45, 20, 0.12);
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
    '<div class="order-title">🍽️ Order Your Favourite Food</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="order-subtitle">'
    'Fresh South Indian Tiffins • Easy Ordering • Delicious Taste ❤️'
    '</div>',
    unsafe_allow_html=True
)

# ==============================
# FOOD DATA
# ==============================

food_items = {
    "Masala Dosa": {
        "price": 80,
        "category": "Tiffins",
        "rating": 4.8,
        "emoji": "🥞"
    },

    "Idli": {
        "price": 40,
        "category": "Tiffins",
        "rating": 4.7,
        "emoji": "🥣"
    },

    "Uttappa": {
        "price": 70,
        "category": "Tiffins",
        "rating": 4.6,
        "emoji": "🍕"
    },

    "Uggani Bajji": {
        "price": 60,
        "category": "Tiffins",
        "rating": 4.7,
        "emoji": "🍽️"
    },

    "Coffee": {
        "price": 30,
        "category": "Drinks",
        "rating": 4.5,
        "emoji": "☕"
    },

    "Green Tea": {
        "price": 25,
        "category": "Drinks",
        "rating": 4.4,
        "emoji": "🍵"
    }
}

# ==============================
# CART
# ==============================

if "order_cart" not in st.session_state:
    st.session_state.order_cart = {}

# ==============================
# SEARCH & CATEGORY
# ==============================

col1, col2 = st.columns(2)

with col1:
    search = st.text_input(
        "🔎 Search Food",
        placeholder="Search dosa, idli, coffee..."
    )

with col2:
    category = st.selectbox(
        "📂 Select Category",
        ["All", "Tiffins", "Drinks"]
    )

# ==============================
# FILTER
# ==============================

filtered_foods = []

for food, details in food_items.items():

    search_match = search.lower() in food.lower()

    category_match = (
        category == "All"
        or details["category"] == category
    )

    if search_match and category_match:
        filtered_foods.append(food)

# ==============================
# FOOD MENU
# ==============================

st.markdown("## 🍴 Our Menu")

for food in filtered_foods:

    details = food_items[food]

    st.markdown(
        '<div class="food-card">',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([4, 2, 1])

    with col1:

        st.markdown(
            f'<div class="food-name">'
            f'{details["emoji"]} {food}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write(
            f'⭐ {details["rating"]}  •  '
            f'{details["category"]}'
        )

    with col2:

        st.markdown(
            f'<div class="price">'
            f'₹{details["price"]}'
            f'</div>',
            unsafe_allow_html=True
        )

    with col3:

        if st.button(
            "➕ Add",
            key=f"order_{food}"
        ):

            if food in st.session_state.order_cart:
                st.session_state.order_cart[food] += 1
            else:
                st.session_state.order_cart[food] = 1

            st.toast(
                f"{food} added to cart! 🛒"
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# ==============================
# CART
# ==============================

st.divider()

st.markdown("## 🛒 Your Cart")

if st.session_state.order_cart:

    st.markdown(
        '<div class="cart-box">',
        unsafe_allow_html=True
    )

    total = 0

    for food, quantity in list(
        st.session_state.order_cart.items()
    ):

        price = food_items[food]["price"]

        item_total = price * quantity

        total += item_total

        col1, col2, col3 = st.columns([4, 2, 1])

        with col1:
            st.write(
                f"🍽️ **{food}**"
            )

        with col2:
            st.write(
                f"₹{price} × {quantity} = "
                f"**₹{item_total}**"
            )

        with col3:

            if st.button(
                "❌",
                key=f"remove_{food}"
            ):

                del st.session_state.order_cart[food]

                st.rerun()

    st.divider()

    st.markdown(
        f"### 💰 Total Bill: ₹{total}"
    )

    if st.button(
        "✅ Place Order",
        use_container_width=True
    ):

        st.balloons()

        st.success(
            "🎉 Order placed successfully! "
            "Thank you for choosing Royal Spice Hotel ❤️"
        )

else:

    st.info(
        "🛒 Your cart is empty. "
        "Add your favourite food from the menu!"
    )

# ==============================
# FOOTER
# ==============================

st.markdown(
    '<div class="footer">'
    '🌶️ <b>Royal Spice Hotel</b><br>'
    'Fresh • Tasty • Smart ❤️'
    '</div>',
    unsafe_allow_html=True
)