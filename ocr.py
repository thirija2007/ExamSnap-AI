import pytesseract
import shutil
from PIL import Image, ImageEnhance, ImageFilter


def extract_text(image):

    # Find Tesseract on Streamlit Cloud
    tesseract_path = shutil.which("tesseract")

    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    try:
        # Convert image to RGB
        image = image.convert("RGB")

        # Enlarge image for better OCR
        width, height = image.size
        image = image.resize(
            (width * 2, height * 2),
            Image.Resampling.LANCZOS
        )

        # Convert to grayscale
        image = image.convert("L")

        # Improve contrast
        image = ImageEnhance.Contrast(image).enhance(2.0)

        # Sharpen image
        image = image.filter(ImageFilter.SHARPEN)

        # Convert to black and white
        image = image.point(
            lambda x: 0 if x < 170 else 255
        )

        # OCR
        text = pytesseract.image_to_string(
            image,
            config="--psm 6"
        )

        return text

    except Exception as e:
        return f"OCR Error: {e}"
