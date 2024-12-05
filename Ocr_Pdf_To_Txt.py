import os
import sys
import time
import argparse
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders


def extract_text_from_pdf(pdf_filename, output_filename, resolution=300, image_format="png", ocr_language="eng"):
    """
    Extracts text from a PDF file using OCR and saves it to a TXT file.

    Args:
        pdf_filename (str): The input PDF file path.
        output_filename (str): The output TXT file path.
        resolution (int): The resolution for PDF rendering (default: 300 dpi).
        image_format (str): Image format for OCR processing (default: 'png').
        ocr_language (str): OCR language code (default: 'eng').
    """
    tools = pyocr.get_available_tools()
    if not tools:
        print("No OCR tool found.")
        sys.exit(1)

    tool = tools[0]
    print(f"Using OCR tool: {tool}")

    # Load and process the PDF
    try:
        pdf_images = Image(filename=pdf_filename, resolution=resolution).convert(image_format)
    except Exception as e:
        print(f"Error loading PDF: {e}")
        sys.exit(1)

    final_text = []
    print(f"Processing PDF: {pdf_filename}")
    start_time = time.time()

    for i, img in enumerate(pdf_images.sequence):
        page_image = Image(image=img)
        page_image.type = 'grayscale'
        page_image.depth = 8

        # Convert to PIL image for OCR processing
        pil_image = PI.open(io.BytesIO(page_image.make_blob(image_format)))

        try:
            page_text = tool.image_to_string(
                pil_image,
                lang=ocr_language,
                builder=pyocr.builders.TextBuilder()
            )
            print(f"Extracted text from page {i + 1}.")
            final_text.append(page_text)
        except Exception as e:
            print(f"Error processing page {i + 1}: {e}")

    elapsed_time = time.time() - start_time
    print(f"PDF processing completed in {elapsed_time:.2f} seconds.")

    # Save the extracted text to the output file
    try:
        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write("\n".join(final_text))
        print(f"Text successfully saved to {output_filename}.")
    except Exception as e:
        print(f"Error saving output file: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from a PDF using OCR and save to TXT.")
    parser.add_argument("pdf_filename", help="Path to the input PDF file.")
    parser.add_argument("output_filename", help="Path to the output TXT file.")
    parser.add_argument("--resolution", type=int, default=300, help="PDF rendering resolution (default: 300 dpi).")
    parser.add_argument("--image_format", type=str, default="png", help="Image format for OCR (default: 'png').")
    parser.add_argument("--ocr_language", type=str, default="eng", help="OCR language code (default: 'eng').")

    args = parser.parse_args()

    if not os.path.isfile(args.pdf_filename):
        print(f"PDF file not found: {args.pdf_filename}")
        sys.exit(1)

    extract_text_from_pdf(
        pdf_filename=args.pdf_filename,
        output_filename=args.output_filename,
        resolution=args.resolution,
        image_format=args.image_format,
        ocr_language=args.ocr_language
    )
