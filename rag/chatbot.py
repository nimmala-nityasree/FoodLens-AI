import os

from dotenv import load_dotenv
import google.generativeai as genai

from rag.retriever import retrieve_context

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_food_ai(question, food_name=None):

    context = retrieve_context(question)

    prompt = f"""
You are an AI Nutrition Assistant.

Use the retrieved knowledge below to answer the question.

Retrieved Knowledge:
{context}

Detected Food:
{food_name}

User Question:
{question}

Rules:
- Answer in simple English.
- Keep it under 150 words.
- Give practical healthy advice.
- If the detected food is available, refer to it naturally.
"""

    response = model.generate_content(prompt)

    return response.text