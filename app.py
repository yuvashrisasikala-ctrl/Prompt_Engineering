import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt

st.set_page_config(
    page_title="AI Prompt Explorer",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Prompt Explorer")
st.caption("Explore. Experiment. Generate.")

st.write(
    "Select a prompting technique, enter your task, "
    "and generate an AI response using Qwen."
)

st.divider()

technique = st.selectbox(
    "🎯 Select Prompting Technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)

task = st.text_area(
    "✍️ Enter Your Task",
    placeholder="Example: Explain Artificial Intelligence in simple words.",
    height=150
)

col1, col2 = st.columns(2)

with col1:
    temperature = st.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.1
    )

with col2:
    max_tokens = st.slider(
        "📝 Maximum Tokens",
        min_value=100,
        max_value=1000,
        value=500,
        step=100
    )

if st.button("✨ Generate Response", use_container_width=True):
    if not task.strip():
        st.warning("Please enter a task first.")
    else:
        try:
            prompt = build_prompt(technique, task)

            st.subheader("🔍 Generated Prompt")
            st.code(prompt, language="text")

            with st.spinner("Qwen is generating your response..."):
                answer = generate_response(
                    prompt,
                    temperature,
                    max_tokens
                )

            st.success("Response Generated Successfully!")

            st.subheader("💡 AI Response")
            st.write(answer)

        except Exception as error:
            st.error(f"Error while generating response: {error}")

st.divider()

st.caption(
    "Built with Python | Streamlit | Hugging Face | Qwen"
)

