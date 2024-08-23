Project Documentation: Automated Tabular Text Extraction

1. Introduction
This project aims to automate the extraction of tabular data from images, converting it into a
structured format like CSV or a DataFrame. The challenge is to accurately detect and extract
text from cells within a table, even when the table structure is complex or when the text may
be slightly misaligned. Various OCR (Optical Character Recognition) models were tested,
including open-source solutions and cloud-based services, to identify the most effective
method for this task. AWS Textract was ultimately selected due to its superior accuracy and
reliability in extracting tabular data.
2. Problem Statement
Given an image containing a table, the goal is to extract the text from each cell and present it
in a structured tabular format. The output should include both a CSV file and a visual
representation of the detected table with bounding boxes around each cell.
3. Technology and Tools
• Programming Language: Python
• Libraries:
o Boto3 for AWS Textract integration
o OpenCV-python for image processing
o PIL (Python Imaging Library) for image handling
o Pandas for DataFrame creation and CSV operations
o NumPy for numerical operations
• OCR Models Tested:
o Pytesseract: Open-source OCR tool with good accuracy on clean, highcontrast text.
o Google Vision: A cloud-based OCR service with advanced capabilities for text
detection.
o EasyOCR: A lightweight OCR tool, particularly effective on images with
clear text.
o AWS Textract: Cloud-based service by Amazon specifically designed for
document analysis, particularly strong in extracting data from tables and
forms.
4. Implementation Details
4.1 Preprocessing
Before passing the image to AWS Textract, basic preprocessing was performed to enhance
text visibility and line detection. This involved converting the image to grayscale, applying
adaptive thresholding, and using morphological operations to highlight horizontal and
vertical lines.
4.2 Text Extraction Using AWS Textract
The core of the project utilizes AWS Textract, which analyses the image to detect blocks of
text, including tables. The service returns a detailed JSON response containing the detected
elements and their bounding boxes.
4.3 Post-processing
After text extraction, the following steps were carried out:
• Table Structure Reconstruction: Based on the row and column indices provided by
AWS Textract, the extracted text was organized into a matrix representing the table
structure.
• DataFrame and CSV Creation: The matrix was converted into a pandas DataFrame
and saved as a CSV file for easy data manipulation and export.
4.4 Visualization
Bounding boxes were drawn around detected cells in the original image to visualize the
accuracy of table detection.
5. Comparative Analysis
During the development process, several OCR models were tested to evaluate their
effectiveness for this specific task:
• Pytesseract: Struggled with tables where text alignment was slightly off or when
lines were not perfectly horizontal or vertical. Required significant preprocessing for
acceptable results.
• Google Vision: Performed well in text detection but was less consistent in
maintaining table structure. Better suited for extracting text blocks rather than
structured tables.
• EasyOCR: Efficient for simple table structures but struggled with complex or dense
tables.
• AWS Textract: Outperformed other models in accurately detecting table structures
and extracting text, even from challenging layouts.
6. Results
AWS Textract provided the most reliable results, with minimal errors in text extraction and
table structure preservation. The output included correctly formatted CSV files and
visualizations with bounding boxes around table cells, highlighting the accurate detection of
rows and columns.
7. Conclusion
For projects requiring the extraction of tabular data from images, AWS Textract is the
recommended tool due to its high accuracy and robustness in handling complex table
structures. While open-source alternatives can be effective in simpler scenarios, Textract's
specialized capabilities in document analysis make it the superior choice for tasks like these.
8. Future Work
Potential improvements include further optimizing the preprocessing steps to handle a
broader range of table layouts and experimenting with other machine learning models to
enhance text detection in specific use cases.
9. Appendix
• Code Snippets:
o AWS Textract Integration: Detailed in the provided code.
o Preprocessing Techniques: Includes thresholding and morphological
operations.
o Comparison of OCR Models: Code for each OCR model tested is available
upon request.
• Sample Images and Output Files: Attached or available in the project repository.
AWS Tesseract:
Threshold Image:
Noice reduced Image: Poor quality and bad in text detection
Vertical and Horizontal Column Detection:
10. References
• AWS Textract Documentation
• OpenCV Documentation
• Pytesseract GitHub Repository
• Google Vision API Documentation
• EasyOCR Documentation
