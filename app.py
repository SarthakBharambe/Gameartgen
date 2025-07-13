import streamlit as st
from PIL import Image
import os
from utils.generator import generate_image
import uuid
import os
from utils.prompts import load_category_prompts




# Set page configuration
st.set_page_config(
    page_title="GameArtGen 🎮",
    page_icon="🎨",
    layout="wide"
)

# Load custom CSS
with open("styles/custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Banner
st.image("assets/ui_banner.png", use_container_width=True)


# Title and description
st.title("🎮 GameArtGen: AI Game Asset Generator")
st.markdown("Create custom characters, weapons, icons, and backgrounds with simple text prompts using Generative AI.")

# Sidebar controls
st.sidebar.header("🧠 Input Settings")
from utils.prompts import load_category_prompts  # ✅ Add this at top

# ✅ Load smart prompt suggestions
category_prompts = load_category_prompts()

# ==========================
# SIDEBAR INPUTS
# ==========================
st.sidebar.header("🧠 Input Settings")

# Step 1: Category selection
category = st.sidebar.selectbox(
    "🎯 Select Category",
    list(category_prompts.keys())  # ✅ dynamic based on file
)

# Step 2: Style selection
style = st.sidebar.selectbox(
    "🎨 Select Style",
    ["Pixel", "Cartoon", "Realistic", "Cyberpunk"]
)

# Step 3: Prompt input box with smart default
default_prompt = category_prompts.get(category, "")
prompt = st.sidebar.text_input(
    "📝 Describe your game asset:",
    value=default_prompt
)

# Step 4: Generate button
generate_btn = st.sidebar.button("🚀 Generate")

# Output area
st.subheader("🖼️ Generated Assets")
if generate_btn:
    try:
        with st.spinner("🎨 Generating image..."):
            full_prompt = f"{prompt}, {style.lower()} style, {category.lower()} asset"
            img = generate_image(full_prompt)

            # Save image with unique name
            unique_filename = f"{category.lower()}_{uuid.uuid4().hex[:8]}.png"
            image_path = f"outputs/{unique_filename}"
            img.save(image_path)

            # Display in gallery
            st.success("✅ Generation complete!")
            st.image(image_path, caption="🖼️ Generated Asset", use_container_width=False, width=300)

            # Add download button
            with open(image_path, "rb") as f:
                st.download_button(
                    label="💾 Download Image",
                    data=f,
                    file_name=unique_filename,
                    mime="image/png"
                )

    except Exception as e:
        st.error(f"❌ Generation failed: {e}")
recent_files = sorted(os.listdir("outputs/"), reverse=True)[:4]

if recent_files:
    st.subheader("🖼️ Recent Generated Assets")
    cols = st.columns(len(recent_files))
    for i, file in enumerate(recent_files):
        with cols[i]:
            st.image(f"outputs/{file}", use_container_width=True)

