import fitz  # PyMuPDF
import json
import os

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.splitext(os.path.basename(pdf_path))[0]

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                text = " ".join([span["text"] for span in line["spans"]]).strip()
                size = max([span["size"] for span in line["spans"]], default=0)
                if not text or len(text) < 3:
                    continue

                if size >= 18:
                    level = "H1"
                elif size >= 14:
                    level = "H2"
                elif size >= 12:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num
                })

    return {
        "title": title,
        "outline": outline
    }

def process_input_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            result = extract_outline(input_path)
            output_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(output_folder, output_filename)
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    process_input_folder("/app/input", "/app/output")
