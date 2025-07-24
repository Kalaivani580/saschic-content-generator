import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

st.set_page_config(page_title="Saschic Content Generator")
st.title("✨ Saschic Content Generator")

content_type = st.selectbox(
    "What do you want to generate?",
    ["Instagram Caption", "Short Story", "Tagline"]
)

product_name = st.text_input("Enter Product or Theme Name (e.g., Wooden Gift Frame)")
audience = st.text_input("Target Audience (e.g., Couples, Kids, Friends, etc.)")

if st.button("Generate"):
    with st.spinner("Generating with magic..."):
        prompt = ""

        if content_type == "Instagram Caption":
            prompt = f"Write an Instagram caption for a product called '{product_name}' for {audience}. Make it emotional or fun."
        elif content_type == "Short Story":
            prompt = f"Write a short, simple story (max 5 lines) about '{product_name}' that would interest {audience}. Use friendly and engaging tone."
        elif content_type == "Tagline":
            prompt = f"Write a catchy one-line Instagram tagline for a product called '{product_name}', targeting {audience}."

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success("Here is your generated content:")
        st.write(response.choices[0].message.content)
