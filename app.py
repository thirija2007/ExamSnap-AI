import streamlit as st
from PIL import Image
import re
import os

from ocr import extract_text
from groq import Groq
from dotenv import load_dotenv


# ==========================================
# LOAD GROQ API KEY
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API key not found in .env file.")
    st.stop()

client = Groq(api_key=api_key)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ExamSnap AI",
    page_icon="📸",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📸 ExamSnap AI")

st.write(
    "Upload any question paper image and generate "
    "AI-based answers for your questions."
)


# ==========================================
# UPLOAD QUESTION PAPER
# ==========================================

uploaded_file = st.file_uploader(
    "📄 Upload Question Paper",
    type=["jpg", "jpeg", "png"]
)


# ==========================================
# PROCESS UPLOADED IMAGE
# ==========================================

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Question Paper")

    st.image(
        image,
        caption="Question Paper",
        width=700
    )


    # ======================================
    # OCR
    # ======================================

    st.subheader("📝 OCR Output")

    try:
        text = extract_text(image)

    except Exception as e:
        st.error(f"OCR Error: {e}")
        st.stop()


    # Check OCR result
    if not text or not text.strip():

        st.error(
            "No text found in the image. "
            "Please upload a clear question paper."
        )

        st.stop()


    # Display OCR text
    st.text_area(
        "Extracted Text",
        text,
        height=250
    )


    # ======================================
    # EXTRACT QUESTIONS
    # ======================================

    questions = re.findall(
        r"((?:Q\s*)?\d+\s*[\.\):\-]\s*.*?)(?=(?:Q\s*)?\d+\s*[\.\):\-]\s*|\Z)",
        text,
        re.DOTALL | re.IGNORECASE
    )


    # ======================================
    # CLEAN QUESTIONS
    # ======================================

    cleaned_questions = []

    for question in questions:

        # Remove new lines
        question = question.replace("\n", " ")

        # Remove unwanted OCR characters
        question = question.replace("“", "")
        question = question.replace("”", "")
        question = question.replace("¥", "")
        question = question.replace('"', "")

        # Remove section headings
        question = re.sub(
            r"Section\s*[A-Z]\s*[-:]?.*?",
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


    # ======================================
    # REMOVE DUPLICATES
    # ======================================

    unique_questions = []

    for question in cleaned_questions:

        if question not in unique_questions:
            unique_questions.append(question)


    # ======================================
    # DISPLAY QUESTIONS
    # ======================================

    st.subheader("📚 Extracted Questions")


    if unique_questions:

        for question in unique_questions:
            st.write("• " + question)


        # ==================================
        # SELECT QUESTION
        # ==================================

        st.subheader("🎯 Select a Question")

        selected_question = st.selectbox(
            "Choose a question:",
            unique_questions
        )


        # ==================================
        # SHOW SELECTED QUESTION
        # ==================================

        st.write("### 📌 Selected Question")

        st.info(selected_question)


        # ==================================
        # GENERATE ANSWER
        # ==================================

        if st.button(
            "🤖 Generate Answer",
            type="primary"
        ):

            with st.spinner(
                "Generating AI answer..."
            ):

                try:

                    response = client.chat.completions.create(

                        model="openai/gpt-oss-20b",

                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are an exam assistant. "
                                    "Answer the given exam question "
                                    "correctly and clearly. "
                                    "Use simple language suitable "
                                    "for college students. "
                                    "Give a well-structured answer. "
                                    "Include examples when useful. "
                                    "Do not discuss unrelated topics."
                                )
                            },
                            {
                                "role": "user",
                                "content": (
                                    "Answer this exam question:\n\n"
                                    + selected_question
                                )
                            }
                        ]
                    )


                    # Get answer
                    answer = response.choices[0].message.content


                    # ==================================
                    # DISPLAY ANSWER
                    # ==================================

                    st.success("✅ Answer Generated")

                    st.subheader("🧠 AI Answer")

                    st.markdown(answer)


                except Exception as e:

                    st.error(
                        f"Error generating answer: {e}"
                    )


    else:

        st.warning(
            "No questions detected. "
            "Please upload a question paper with "
            "numbered questions such as 1., 2., 3. "
            "or Q1., Q2., Q3."
        )
