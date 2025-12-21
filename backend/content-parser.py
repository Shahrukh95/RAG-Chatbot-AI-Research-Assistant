import pymupdf


def extract_text_by_page(pdf_path: str, start_page: int, end_page: int) -> list[str]:
    """Extracts text content from a range of pages in a PDF file.

    Args:
        pdf_path (str): The file path to the PDF document.
        start_page (int): The starting page number (1-based index).
        end_page (int): The ending page number (inclusive, 1-based index).

    Returns:
        list[str]: A list of strings, each containing the extracted text from a page within the specified range.
    """

    doc = pymupdf.open(pdf_path) # open the document
    content = []
    for i in range(start_page - 1, end_page):
        page_doc = doc[i]
        text = page_doc.get_text()
        content.append(text)

    return content


# content_array = extract_text_by_page("backend/data/uploads/pre-interview.pdf", 2, 3)
# for page in content_array:
#     print(page + "\n\n\n\n")


