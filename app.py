import streamlit as st
from story_generator import StoryGenerator

st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("📚 AI Story Generator")
st.markdown("Generate creative short stories using AI.")

story_gen = StoryGenerator()

prompt = st.text_area("✏️ Enter a story prompt", height=100)
max_length = st.slider("📏 Story length (words)", 100, 600, 300, step=50)

if st.button("🚀 Generate Story"):
    with st.spinner("Generating your story..."):
        full_prompt = f"Continue this story: {prompt.strip()}"
        story = story_gen.generate_story(full_prompt, max_length=max_length)
        st.subheader("📖 Your Story")
        st.write(story)
