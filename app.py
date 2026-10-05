import streamlit as st
from PIL import Image
import re
import os

from ocr import extract_text
from groq import Groq
from dotenv import load_dotenv


# Load API key from .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API key not found. Please add it to the .env file.")
    st.stop()

client = Groq(api_key=api_key)


# Page title
st.title("📸 ExamSnap AI")

st.write(
    "Upload a question paper image and get AI-generated answers."
)


# Upload question paper
file = st.file_uploader(
    "Upload Question Paper",
    type=["jpg", "jpeg", "png"]
)


if file:

    # Display uploaded image
    image = Image.open(file)

    st.subheader("📷 Uploaded Question Paper")
    st.image(image, width=600)


    # OCR
    text = extract_text(image)


    if not text.strip():
        st.error("No text found in the image.")
        st.stop()


    # OCR Output
    st.subheader("📝 OCR Output")

    st.text_area(
        "Extracted Text",
        text,
        height=250
    )


    # Extract individual questions
    questions = re.findall(
        r"(Q\d+\..*?)(?=\s*Q\d+\.|\Z)",
        text,
        re.DOTALL
    )


    # Clean questions
    cleaned_questions = []

    for question in questions:

        # Remove new lines
        question = question.replace("\n", " ")

        # Remove unwanted OCR symbols
        question = question.replace("“", "")
        question = question.replace("”", "")
        question = question.replace("¥", "")
        question = question.replace('"', "")

        # Remove Section B heading if attached
        question = re.sub(
            r"\s*Section B\s*-\s*Applications.*?$",
            "",
            question,
            flags=re.IGNORECASE
        )

        # Remove extra spaces
        question = re.sub(
            r"\s+",
            " ",
            question
        )

        question = question.strip()

        if question:
            cleaned_questions.append(question)


    # Display extracted questions
    st.subheader("📚 Extracted Questions")


    if cleaned_questions:

        for question in cleaned_questions:
            st.write("• " + question)


        # Question selection
        st.subheader("🎯 Select a Question")

        selected_question = st.selectbox(
            "Choose a question:",
            cleaned_questions
        )


        # Selected question
        st.write("### Selected Question")

        st.info(selected_question)


        # AI Answer
        st.write("### 🤖 AI Answer")


        if st.button("Generate Answer"):

            with st.spinner("Generating answer..."):

                try:

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-20b",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are an exam assistant. "
                                    "Give clear, correct and easy-to-understand "
                                    "answers suitable for college students. "
                                    "Explain the answer briefly and clearly."
                                )
                            },
                            {
                                "role": "user",
                                "content": (
                                    f"Answer this exam question:\n\n"
                                    f"{selected_question}"
                                )
                            }
                        ]
                    )


                    answer = response.choices[0].message.content


                    st.success("✅ Answer Generated")

                    st.write(answer)


                except Exception as e:

                    st.error(
                        f"Error generating answer: {e}"
                    )


    else:

        st.warning("No questions detected.")