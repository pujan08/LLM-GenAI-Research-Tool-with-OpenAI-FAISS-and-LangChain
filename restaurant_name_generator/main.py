import streamlit as st
import langchain_helper

# Set the page configuration (title, icon, layout)
st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Background color */
    .stApp {
        background-color: #f0f2f6;
    }
    /* Title style */
    h1 {
        color: #FF6347;  /* Tomato color */
        font-family: 'Arial Black', sans-serif;
        text-align: center;
    }
    /* Sidebar style */
    .css-1d391kg {
        background-color: #f7e7ce;
    }
    /* Header style */
    .css-2trqyj {
        color: #4682B4;  /* Steel Blue */
        font-family: 'Verdana', sans-serif;
    }
    /* Subheader style */
    .css-1j77nb6 {
        color: #4682B4;
        font-family: 'Verdana', sans-serif;
    }
    /* Menu items style */
    .stText {
        font-family: 'Georgia', serif;
        color: #333333;
    }
    /* Sidebar selectbox */
    .css-10trblm {
        color: #FF6347;
    }
    /* Add some padding */
    .css-1oe5cao {
        padding: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Restaurant Name Generator")

# Sidebar for cuisine selection
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Canadian", "Mexican"))

# Generate and display restaurant name and menu items
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    st.subheader("MENU Items")

    # Clean and format the menu items
    menu_items = [item.strip().lstrip('0123456789. ') for item in response['menu_items'].strip().split(",")]

    # Display each menu item with proper numbering
    for idx, item in enumerate(menu_items, start=1):
        st.write(f"{idx}. {item}")

# Continue with the rest of your imports and functions...
