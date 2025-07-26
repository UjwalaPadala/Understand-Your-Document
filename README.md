
## Challenge: PDF Outline Extraction

The task is to extract a structured outline from a PDF file, including:

- Document Title
- Section Headings (H1, H2, H3)
- Page Numbers

This solution runs inside a Docker container and processes all PDF files in a given `/input` folder. The output is a corresponding `.json` file per PDF, saved in `/output`.

---

## How to Build the Docker Image

Run this command from the root folder:

```bash
docker build --platform linux/amd64 -t pdf_outline:v1 .
