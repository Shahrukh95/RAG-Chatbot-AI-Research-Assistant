import pymupdf
import os

# PATHS
CURRENT_PATH = os.getcwd()
TEST_UPLOADS = os.path.join(CURRENT_PATH, "output_testing/images") 
os.makedirs(TEST_UPLOADS, exist_ok=True)


def extract_text_and_images_by_page(pdf_path: str, start_page: int = None, end_page: int = None) -> list[str]:
    """
    Extracts text content from a range of pages in a PDF file and saves images found on those pages.

    Args:
        pdf_path (str): The file path to the PDF document.
        start_page (int, optional): The starting page number (1-based index). Defaults to 1.
        end_page (int, optional): The ending page number (inclusive, 1-based index). Defaults to last page.

    Returns:
        list[str]: A list of strings, each containing the extracted text from a page within the specified range.

    Raises:
        ValueError: If the page range is invalid or a page does not exist.

    Side Effects:
        Saves images found on each page to the TEST_UPLOADS directory (if image saving is enabled).
    """

    doc = pymupdf.open(pdf_path) # open the document
    filename = os.path.basename(pdf_path)
    print(filename)
    content = []

    num_pages = len(doc)
    start_page = 1 if start_page is None else start_page
    end_page = num_pages if end_page is None else end_page

    # Validate page range
    if start_page < 1 or end_page > num_pages or start_page > end_page:
        raise ValueError(f"Invalid page range: {start_page} to {end_page} for document with {num_pages} pages.")
    
    for i in range(start_page - 1, end_page):
        try:
            page_doc = doc[i]
            text = page_doc.get_text()
            content.append(text)

            image_list = page_doc.get_images()
            # print(image_list)
            print_number_of_images(image_list=image_list, page_index=i)
            save_images(doc=doc, page_index=i, image_list=image_list, pdf_path=pdf_path, filename=filename)
            
        except Exception as e:
            raise ValueError(f"Page {i+1} does not exist")

    return content

def print_number_of_images(image_list, page_index):
    """
    Prints the number of images found on a given PDF page.

    Args:
        image_list (list): List of images found on the page.
        page_index (int): The index of the page (0-based).
    """
    if image_list:
        print(f"Found {len(image_list)} images on page {page_index+1}")
    else:
        print("No images found on page", page_index+1)


def save_images(doc, page_index, image_list, pdf_path, filename):
    """
    Saves images from a PDF page to the TEST_UPLOADS directory.

    Args:
        doc: The opened PDF document object.
        page_index (int): The index of the page (0-based).
        image_list (list): List of images found on the page.

    Side Effects:
        Saves each image as a PNG file in the TEST_UPLOADS directory.
    """
    
    filename = os.path.basename(pdf_path)  # e.g., file1.pdf
    folder_path = os.path.join(TEST_UPLOADS, filename)
    os.makedirs(folder_path, exist_ok=True)

    for image_index, img in enumerate(image_list, start=1): # enumerate the image list
        xref = img[0] # get the XREF of the image
        pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

        if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

        # save the image as png
        pix.save(os.path.join(folder_path, f"page_{page_index+1}-image_{image_index}.png"))
        # free image memory
        pix = None 


# content_array = extract_text_and_images_by_page("backend/data/uploads/file2.pdf", 1, 2)
# print(content_array)




