import os
import pytesseract
os.environ['TESSDATA_PREFIX'] = 'C:/Program Files/Tesseract-OCR/tessdata'
# Set the path to Tesseract-OCR executable if it's not in your PATH environment variable
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Replace with the actual path

print(pytesseract.get_tesseract_version())

from PIL import Image
import cv2
import pandas as pd

# If Tesseract is not in your PATH, specify the path directly
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """Preprocess the image for better OCR results"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return gray

def extract_text_from_image(image_path):
    """Extract text from the image using Tesseract OCR"""
    img = preprocess_image(image_path)
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    return data, img

def draw_bounding_boxes(data, img):
    """Draw bounding boxes around detected text"""
    n_boxes = len(data['text'])
    for i in range(n_boxes):
        if int(data['conf'][i]) > 60:  # confidence threshold
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(img, data['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


def create_table(data):
    """Create a table from the extracted OCR data"""
    table = {'Signature': [], 'Printed Name': [], 'Street and Number': [], 
             'City': [], 'Phone Number': [], 'Email': [], 'Date': []}
    
    n_boxes = len(data['text'])
    row = 0
    for i in range(n_boxes):
        if int(data['conf'][i]) > 60:  # confidence threshold
            text = data['text'][i]
            if row % 7 == 0:
                table['Signature'].append(text)
            elif row % 7 == 1:
                table['Printed Name'].append(text)
            elif row % 7 == 2:
                table['Street and Number'].append(text)
            elif row % 7 == 3:
                table['City'].append(text)
            elif row % 7 == 4:
                table['Phone Number'].append(text)
            elif row % 7 == 5:
                table['Email'].append(text)
            elif row % 7 == 6:
                table['Date'].append(text)
            row += 1

    # Ensure all lists are of the same length
    max_len = max(len(col) for col in table.values())
    for key in table:
        while len(table[key]) < max_len:
            table[key].append('')

    return pd.DataFrame(table)


def main(image_path):
    data, img = extract_text_from_image(image_path)
    table = create_table(data)
    print(table)
    
    # Draw bounding boxes and labels
    draw_bounding_boxes(data, img)
    
    # Show the image with bounding boxes
    cv2.imshow('Detected Text', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the image with bounding boxes
    output_path = 'output_with_boxes.jpg'
    cv2.imwrite(output_path, img)
    print(f'Image saved as {output_path}')

if __name__ == "__main__":
    image_path = 'image1.jpg'  # Replace with your image path
    main(image_path)
