# bulk-image-downloader
A Python script to bulk download images from a CSV export (Shopify-style) with progress tracking.
# Bulk Image Downloader from CSV

This project contains a Python script designed to automate the download of images from a CSV file (like Shopify product exports). It reads image URLs and product handles, downloads each image, and saves them to a local `Images/` directory.

## Features
- Reads image URLs from a CSV file
- Saves images with clean filenames
- Tracks download progress using `tqdm`
- Handles connection errors and failed downloads

## Requirements
- Python 3.x
- `requests`
- `tqdm`

Install dependencies:
```bash
pip install requests tqdm
````
How to Use
Place your CSV file in the same folder and name it products_export.csv.
Make sure the CSV includes the following columns:

Run the script:
python download-images.py*

All images will be saved in the Images/ folder.
