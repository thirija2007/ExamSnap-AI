import pytesseract
import shutil

def extract_text(image):
    tesseract_path = shutil.which("tesseract")

    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    try:
        return pytesseract.image_to_string(image)
    except Exception as e:
        return f"OCR Error: {e}"
