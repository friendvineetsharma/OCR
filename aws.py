import boto3
import cv2
import numpy as np
from PIL import Image
import io
import pandas as pd  # Import pandas for DataFrame and CSV operations

def draw_boxes(image, blocks, key_map, color=(0, 0, 255)):
    img = np.array(image)
    for block in blocks:
        if 'Geometry' in block and 'Polygon' in block['Geometry']:
            points = block['Geometry']['Polygon']
            pts = np.array([[int(point['X'] * img.shape[1]), int(point['Y'] * img.shape[0])] for point in points])
            cv2.polylines(img, [pts], isClosed=True, color=color, thickness=2)
            if block['Id'] in key_map:
                text = key_map[block['Id']]
                cv2.putText(img, text, tuple(pts[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
    return img

def get_text_from_blocks(blocks):
    block_map = {}
    table_blocks = []
    for block in blocks:
        block_map[block['Id']] = block
        if block['BlockType'] == "TABLE":
            table_blocks.append(block)

    tables = []
    for table in table_blocks:
        table_data = []
        for relationship in table.get('Relationships', []):
            if relationship['Type'] == 'CHILD':
                for cell_id in relationship['Ids']:
                    cell = block_map[cell_id]
                    if cell['BlockType'] == 'CELL':
                        cell_text = []
                        for cell_rel in cell.get('Relationships', []):
                            if cell_rel['Type'] == 'CHILD':
                                for word_id in cell_rel['Ids']:
                                    word = block_map[word_id]
                                    cell_text.append(word['Text'])
                        table_data.append({
                            'RowIndex': cell['RowIndex'],
                            'ColumnIndex': cell['ColumnIndex'],
                            'Text': " ".join(cell_text)
                        })
        tables.append(table_data)
    return tables

def extract_table_from_image(image_path):
    with open(image_path, 'rb') as document:
        imageBytes = document.read()

    # Create a Textract client
    textract = boto3.client('textract')

    # Call Amazon Textract to analyze the document
    response = textract.analyze_document(
        Document={'Bytes': imageBytes},
        FeatureTypes=["TABLES"]
    )

    # Extract blocks from the response
    blocks = response['Blocks']

    # Extract table text
    tables = get_text_from_blocks(blocks)

    # Load the image
    image = Image.open(io.BytesIO(imageBytes))

    # Map block IDs to text for labeling
    key_map = {block['Id']: block['Text'] for block in blocks if 'Text' in block}

    # Draw bounding boxes around table cells
    img_with_boxes = draw_boxes(image, blocks, key_map)

    # Save and display the result
    img_with_boxes = cv2.cvtColor(img_with_boxes, cv2.COLOR_RGB2BGR)
    cv2.imwrite('output_textract_table.jpg', img_with_boxes)
    cv2.imshow('Detected Table', img_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print and save extracted tables to CSV and DataFrame
    for table in tables:
        # Find the maximum row and column indices to determine the table size
        max_row = max([cell['RowIndex'] for cell in table])
        max_col = max([cell['ColumnIndex'] for cell in table])
        
        # Initialize a matrix for the table
        table_matrix = [["" for _ in range(max_col)] for _ in range(max_row)]
        
        # Populate the matrix with the extracted text
        for cell in table:
            row_idx = cell['RowIndex'] - 1  # Adjusting to 0-based index
            col_idx = cell['ColumnIndex'] - 1  # Adjusting to 0-based index
            table_matrix[row_idx][col_idx] = cell['Text']
        
        # Create a DataFrame from the matrix
        df = pd.DataFrame(table_matrix)
        
        # Save the DataFrame to a CSV file
        table_csv_filename = f'table_{tables.index(table)}.csv'
        df.to_csv(table_csv_filename, index=False, header=False)
        print(f'Saved table to {table_csv_filename}')

# Replace with the path to your image file
image_path = 'image.jpg'
extract_table_from_image(image_path)
