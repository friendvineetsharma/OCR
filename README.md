Table Extraction from Images using AWS Textract

Overview:
This project demonstrates the extraction of tabular data from images using AWS Textract. The primary goal is to accurately detect and extract tables from images and represent them in a structured, tabular format. This process is particularly useful for digitizing and automating the extraction of information from scanned documents, forms, and tables.

Features:
AWS Textract Integration: Leverages AWS Textract's powerful OCR capabilities to detect and extract tabular data from images.

Bounding Box Visualization: Draws bounding boxes around detected tables and cells in the image to visually confirm the detection accuracy.

CSV Export: Extracted tables are saved as CSV files for easy integration with other data processing workflows.

Comparison with Other OCR Tools: The project also includes code and analysis for other OCR tools like Google Tesseract, Google Vision, and EasyOCR, providing a comparative study of their effectiveness against AWS Textract.


Installation
Clone the Repository:

git clone https://github.com/your-username/table-extraction.git

cd table-extraction


Install Dependencies:

Ensure you have Python 3.x installed. Install the required Python packages:

pip install boto3 opencv-python-headless numpy pillow pandas


AWS Setup:

Configure your AWS credentials to access AWS Textract. You can do this by setting up a ~/.aws/credentials file with your credentials or by using environment variables.

Ensure you have the necessary permissions for AWS Textract.


Usage
Extract Table from an Image:

Replace image.jpg with the path to your image file.

python extract_table_from_image.py

Review Extracted Tables:

The extracted tables will be saved as CSV files in the project directory. The image with detected tables and bounding boxes will also be saved and displayed.

Compare with Other OCR Tools:

The repository contains additional scripts to compare the performance of AWS Textract with Tesseract, Google Vision, and EasyOCR. The comparison includes the accuracy of text extraction and the quality of the output table.

Project Structure:

extract_table_from_image.py: Main script for extracting tables from images using AWS Textract.

tesseract_ocr.py: Script for extracting text using Tesseract OCR (optional).

google_vision_ocr.py: Script for extracting text using Google Vision (optional).

easyocr_extraction.py: Script for extracting text using EasyOCR (optional).

README.md: Project documentation.


Results

Accuracy: AWS Textract provided the highest accuracy in extracting tabular data from images.

Efficiency: Textract's performance was more reliable compared to other OCR tools, especially in complex table structures.


Future Work

Confusion Matrix & AUC Curve: Future enhancements could include developing a confusion matrix, precision table, and AUC curve for evaluating model performance.

Support for Complex Tables: Enhance the model to handle more complex table structures, including nested tables and merged cells.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Special thanks to the developers and contributors of AWS Textract, Tesseract OCR, Google Vision, and EasyOCR.
