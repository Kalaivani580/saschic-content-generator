import streamlit as st

st.set_page_config(page_title="✨ Saschic Content Generator", page_icon="✨")

st.title("✨ Saschic Content Generator")

# Dropdown for content type
content_type = st.selectbox(
    "What do you want to generate?",
    ["Instagram Caption", "Short Story", "Tagline"],
    key="selectbox_content_type"
)

# Product/Theme input
product_name = st.text_input(
    "Enter Product or Theme Name (e.g., Wooden Gift Frame)",
    key="input_product"
)

# Target Audience input
audience = st.text_input(
    "Target Audience (e.g., Couples, Kids, Friends, etc.)",
    key="input_audience"
)

# Submit button
if st.button("Generate", key="button_generate"):
    if content_type == "Instagram Caption":
        caption = f"💖 Celebrate moments with our {product_name}! Perfect for {audience} who love unique memories. 🖼️✨ #SaschicStyle"
        st.subheader("Here is your generated caption:")
        st.success(caption)

    elif content_type == "Short Story":
        story = (
            f"Once upon a time not too long ago, a happily-engaged couple discovered a charming little store. "
            f"There, they found our beautiful {product_name}, crafted with love and care. They placed their favourite "
            f"memory in it, and from that day, it became a part of their cozy love story. Perfect for {audience} looking to "
            f"capture moments that matter. 💑✨"
        )
        st.subheader("Here is your generated story:")
        st.success(story)

    elif content_type == "Tagline":
        tagline = f"{product_name}: Crafted for {audience}, Cherished Forever. ✨"
        st.subheader("Here is your generated tagline:")
        st.success(tagline)
