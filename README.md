#  ExamSnap AI – Intelligent Question Paper Scanner & Answer Assistant

ExamSnap AI is an AI-powered web application that scans question paper images, extracts questions using Optical Character Recognition (OCR), and generates clear answers using Artificial Intelligence.

The application helps students quickly convert question paper images into digital questions and get AI-generated answers for selected questions.

---

##  Project Overview

ExamSnap AI combines **OCR technology** and **Generative AI** to create a simple question paper assistant.

Instead of manually typing questions from a question paper, users can upload an image of the question paper. The application automatically extracts the questions and allows the user to select any question to generate an AI-based answer.

##  Live Demo

 Try ExamSnap AI here:

 https://examsnap-ai-mmisk2nfyean4vgyjuqvii.streamlit.app/

### Main Workflow

**Question Paper Image**
↓

**OCR Text Extraction**
↓

**Question Detection**
↓

**Question Selection**
↓

**AI Answer Generation**
↓

**Answer Display**

---

##  Objectives

The main objectives of ExamSnap AI are:

* To reduce manual typing of questions from question papers.
* To extract questions automatically from images.
* To use OCR for converting image text into digital text.
* To provide AI-generated answers for selected questions.
* To create a simple and user-friendly student assistant.
* To demonstrate the integration of OCR and Generative AI.

---

##  Features

*  Upload question paper images
*  Extract text using OCR
*  Convert image-based questions into digital text
*  Automatically detect individual questions
*  Select a question from the extracted list
*  Generate answers using Generative AI
*  Provide simple and easy-to-understand explanations
*  Fast AI-powered response
*  Streamlit-based interactive web interface

---

##  How ExamSnap AI Works

### 1. Upload Question Paper

The user uploads a question paper image in JPG, JPEG, or PNG format.

### 2. OCR Processing

The uploaded image is processed using **Tesseract OCR**.

OCR converts the text present in the image into machine-readable text.

### 3. Question Extraction

The extracted OCR text is processed using Python Regular Expressions.

The application identifies questions such as:

```text
Q1. What is Artificial Intelligence?
Q2. Define Machine Learning.
Q3. What is Deep Learning?
Q4. Explain the Applications of Artificial Intelligence.
Q5. What is Natural Language Processing?
```

### 4. Question Selection

The extracted questions are displayed in the application.

The user can select a particular question from the dropdown menu.

### 5. AI Answer Generation

The selected question is sent to a Generative AI model through the Groq API.

The AI generates a clear and student-friendly answer.

### 6. Answer Display

The generated answer is displayed directly in the Streamlit application.

---

##  Technologies Used

| Technology          | Purpose                            |
| ------------------- | ---------------------------------- |
| Python              | Main programming language          |
| Streamlit           | Web application interface          |
| Tesseract OCR       | Extract text from images           |
| Pytesseract         | Python interface for Tesseract OCR |
| Pillow              | Image processing                   |
| Groq API            | AI answer generation               |
| GPT-OSS-20B         | Generative AI model                |
| Python-dotenv       | Local API key management           |
| Regular Expressions | Question extraction                |

---

##  Project Structure

```text
ExamSnap-AI/
│
├── app.py
├── ocr.py
├── requirements.txt
├── packages.txt
├── .gitignore
└── README.md
```

### File Description

#### `app.py`

Contains the main Streamlit application.

It handles:

* Image uploading
* OCR processing
* Question extraction
* Question selection
* AI answer generation
* Answer display

#### `ocr.py`

Contains the OCR functionality using Pytesseract.

#### `requirements.txt`

Contains the Python packages required to run the application.

#### `packages.txt`

Contains the system package required for Tesseract OCR on Streamlit Cloud.

#### `.gitignore`

Prevents sensitive files such as `.env` from being uploaded to GitHub.

#### `README.md`

Contains the documentation of the project.

---

##  Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ExamSnap-AI.git
```

### Step 2: Open the Project Folder

```bash
cd ExamSnap-AI
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

---

##  API Key Setup

ExamSnap AI uses the Groq API for AI answer generation.

### For Local Development

Create a file named:

```text
.env
```

Inside the `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

Do not upload the `.env` file to GitHub.

The `.gitignore` file should contain:

```text
.env
__pycache__/
*.pyc
```

---

##  Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your web browser.

---

##  Application Interface

The application contains the following sections:

### 📸 ExamSnap AI

Main title of the application.

###  Uploaded Question Paper

Displays the uploaded question paper image.

###  OCR Output

Displays the text extracted from the image.

###  Extracted Questions

Displays the individual questions detected from the OCR output.

###  Select a Question

Allows the user to select a question.

###  AI Answer

Generates and displays an AI-based answer for the selected question.

<img width="1075" height="847" alt="Screenshot 2026-10-05 164106" src="https://github.com/user-attachments/assets/d33bcea2-5717-452f-8434-772b9513d82d" />
<img width="958" height="751" alt="Screenshot 2026-10-05 164124" src="https://github.com/user-attachments/assets/0b47b47e-948b-4874-bc91-f1eb7bb1f698" />
<img width="1042" height="822" alt="Screenshot 2026-10-05 164146" src="https://github.com/user-attachments/assets/d23b2303-bfa7-46e2-b0fd-ed14b37e86fe" />

---

##  Example

### Input

A question paper image containing:

```text
Q1. What is Artificial Intelligence?

Q2. Define Machine Learning.

Q3. What is Deep Learning?

Q4. Explain the Applications of Artificial Intelligence.

Q5. What is Natural Language Processing?
```

### Extracted Output

```text
Q1. What is Artificial Intelligence?
Q2. Define Machine Learning.
Q3. What is Deep Learning?
Q4. Explain the Applications of Artificial Intelligence.
Q5. What is Natural Language Processing?
```

### Selected Question

```text
Q3. What is Deep Learning?
```

### AI Generated Answer

```text
Deep Learning is a subset of Machine Learning that uses
artificial neural networks with multiple layers to learn
complex patterns from large amounts of data.

It is commonly used in image recognition, speech recognition,
natural language processing, and other AI applications.
```

---

##  Deployment

ExamSnap AI can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in using your GitHub account.
4. Select the ExamSnap AI repository.
5. Select `app.py` as the main file.
6. Add the Groq API key under **Secrets**.
7. Deploy the application.

### Streamlit Secrets

For deployment, add the API key in Streamlit Secrets:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never upload the actual API key to GitHub.

---

##  Security

The Groq API key is treated as a secret.

For local development:

```text
.env
```

is used to store the API key.

For deployment:

```text
Streamlit Secrets
```

is used.

The `.env` file is excluded from GitHub using `.gitignore`.

---

##  Future Enhancements

The project can be improved with additional features such as:

*  Support for PDF question papers
*  Multi-page question paper processing
*  Better OCR accuracy
*  2-mark, 5-mark, and 10-mark answer modes
*  Detailed answer explanations
*  Topic-wise question classification
*  Text-to-speech for answers
*  Download answers as PDF
*  Support for multiple languages
*  Question paper analysis
*  Important-question detection

---

##  Project Workflow

```text
              ┌─────────────────────┐
              │ Question Paper Image│
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │     Tesseract OCR   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Extracted OCR Text │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Question Extraction │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Select a Question  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Groq AI Model    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    AI Generated     │
              │       Answer        │
              └─────────────────────┘

---

##  Requirements

The project requires:

```text
streamlit
pillow
pytesseract
groq
python-dotenv
```

These dependencies are included in `requirements.txt`.

---

##  Conclusion

ExamSnap AI demonstrates how **OCR and Generative AI** can be combined to create an intelligent question paper assistant.

The system automatically extracts questions from question paper images and generates AI-based answers for selected questions, making exam preparation faster and easier.

##  Developed By

**Thirija R**

B.Sc. Computer Science with Artificial Intelligence

---
