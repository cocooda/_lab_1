import streamlit as st
from template import compare_models

st.set_page_config(page_title="LLM Comparison Demo", page_icon="🤖", layout="wide")

st.title("🤖 GPT-4o vs GPT-4o-mini")
st.write("Compare the same prompt across both models with an easy or full interface mode.")

with st.sidebar:
    st.header("Interface")
    ui_mode = st.radio(
        "Select view mode",
        ["Easy", "Full"],
        index=0,
        help="Choose Easy for a minimal interface or Full for extra guidance and details.",
    )

    if ui_mode == "Full":
        st.markdown("### Prompt tips")
        st.markdown("- Keep the prompt clear and focused.")
        st.markdown("- Compare both model outputs with the same prompt.")
        st.markdown("- Use the expander after running to inspect details.")
    else:
        st.info("Easy mode: type a prompt and compare both models.")

prompt = st.text_area(
    "Enter your prompt",
    "Explain the difference between temperature and top_p.",
    height=180,
)

run_compare = st.button("Compare Models")

if run_compare:
    with st.spinner("Calling OpenAI..."):
        result = compare_models(prompt)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("GPT-4o")
        st.write(result["gpt4o_response"])
        st.caption(f"Latency: {result['gpt4o_latency']:.2f}s")
        st.metric("Estimated GPT-4o cost", f"${result['gpt4o_cost_estimate']:.6f}")

    with col2:
        st.subheader("GPT-4o-mini")
        st.write(result["mini_response"])
        st.caption(f"Latency: {result['mini_latency']:.2f}s")

    with st.expander("Prompt & settings details"):
        st.write("**Prompt**")
        st.code(prompt)
        st.write("**Interface mode**")
        st.write(f"- {ui_mode} mode")
        st.write("The same prompt was sent to both models for a direct side-by-side comparison.")