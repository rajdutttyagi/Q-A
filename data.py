import fitz
import os

def extract_tables(folder="documents_all"):
    results = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            doc = fitz.open(path)

            for page_num, page in enumerate(doc, start=1):  
                tables = page.find_tables()
                
                if tables:
                    actual_tables = [table for table in tables if table.extract()]
                    for table_index, table in enumerate(actual_tables, start=1):
                        table_data = table.extract()
                        results.append({
                            "filename": filename,
                            "page": page_num,
                            # "table_index": table_index,
                            "table_data": table_data
                        })

            doc.close()
    return results




def extract_img(folder="documents_all"):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            doc = fitz.open(path)

            for page_num, page in enumerate(doc, start=1): 
                # Pure page ka text
                page_text = page.get_text("text") 

                # Images extract
                image_list = page.get_images(full=True)

                if image_list:
                    for img_index, img in enumerate(image_list):
                        xref = img[0]
                        base_image = doc.extract_image(xref)

                        image_bytes = base_image["image"]

                        # Preceding text
                        preceding_text = page_text.strip()

                        images.append({
                            "filename": filename,
                            "page": page_num,
                            "image_index": img_index,
                            "image_bytes": image_bytes,
                            "preceding_text": preceding_text
                        })

            doc.close()
    return images






def extract_text(folder="documents_all"):
    results = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            doc = fitz.open(path)

            for page_num, page in enumerate(doc, start=1):  # Pages start from 1
                text = page.get_text("text").strip()
                if text:
                    results.append({
                        "filename": filename,
                        "page": page_num,
                        "text": text
                    })

            doc.close()
    return results
