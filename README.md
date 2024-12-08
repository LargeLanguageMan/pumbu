# Pembukuan for Shopee and Tokopedia

A Streamlit web application to format and analyze sales data from Shopee and Tokopedia e-commerce platforms.

## Features

- Upload and process .xlsx files from Shopee or Tokopedia
- Clean and standardize data format
- Display key metrics:
  - Most sold item
  - Total revenue
  - Total quantity sold
- Easy data export with clipboard functionality

## Installation

1. Clone this repository
2. Install the required dependencies: 
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run main.py
```

## Required Dependencies

- streamlit
- pandas
- numpy
- openpyxl

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```
2. Select your e-commerce platform (Shopee or Tokopedia)
3. Upload your .xlsx file
4. View the processed data and metrics
5. Copy the formatted data to clipboard with one click

## Data Processing

### Shopee
- Filters relevant columns (Status, Payment Time, Product Name, Quantity, etc.)
- Removes cancelled orders
- Formats payment dates
- Converts numeric values
- Calculates sales metrics

### Tokopedia
- Handles specific Tokopedia Excel format
- Cleans header rows
- Formats payment dates
- Calculates total revenue
- Processes relevant sales data

## Contributing

Feel free to open issues or submit pull requests for any improvements.


