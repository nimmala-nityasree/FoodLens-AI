import streamlit as st
import tempfile

from cnn.predictor import predict_food
from utils.nutrition import get_nutrition, get_recommendation
from rag.chatbot import ask_food_ai

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="FoodLens AI",
    page_icon="🍽️",
    layout="wide"
)

st.markdown(
    """
    <h1 class="main-title">🍽️ FoodLens AI</h1>
    <p class="sub-title">
        AI-Powered Food Recognition & Nutrition Recommendation System
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------------- IMAGE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📸 Upload a food image",
    type=["jpg", "jpeg", "png"]
)

food_name = None

if uploaded_file is not None:

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    # Predict food
    prediction = predict_food(temp_path)
    food_name = prediction["food"]

    # Get nutrition
    nutrition = get_nutrition(food_name)

    # Get recommendation
    recommendation = get_recommendation(food_name)

    with col2:

        st.success("Prediction Complete")

        st.subheader("🍴 Food Detected")
        st.write(food_name.title())

        st.subheader("🎯 Confidence")
        st.progress(prediction["confidence"] / 100)
        st.write(f"**{prediction['confidence']}%**")

        st.divider()

        st.subheader("🥗 Nutrition")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Calories", nutrition["Calories"])
            st.metric("Protein", nutrition["Protein"])

        with c2:
            st.metric("Carbs", nutrition["Carbs"])
            st.metric("Fat", nutrition["Fat"])

        st.divider()

        st.subheader("💡 Recommendation")
        st.info(recommendation)

# ---------------- AI CHATBOT ---------------- #

st.divider()

st.header("💬 AI Nutrition Assistant")

question = st.text_input(
    "Ask a question about your food...",
    placeholder="Example: Is pizza healthy?"
)

if st.button("Ask AI"):

    if question.strip():

        with st.spinner("Thinking... 🤖"):

            answer = ask_food_ai(question, food_name)

        st.success(answer)

    else:
        st.warning("Please enter a question.")