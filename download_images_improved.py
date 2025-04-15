
import csv
import os
import requests
import sys
import re
from tqdm import tqdm

def sanitize_filename(name):
    """Remove unsafe characters from filenames."""
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def download_images(csv_file, output_dir="Images", handle_header="Handle", image_src_header="Image Src"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csv_file, "r", encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        rows = [row for row in csv_reader if row.get(handle_header) and row.get(image_src_header)]
        total_images = len(rows)

        print(f"Total images to download: {total_images}")
        progress_bar = tqdm(total=total_images, desc="Downloading images")

        for row in rows:
            handle = sanitize_filename(row[handle_header].strip())
            img_url = row[image_src_header].strip()

            try:
                response = requests.get(img_url, timeout=10)
                if response.status_code == 200:
                    image_name = img_url.split("/")[-1].split("?")[0]
                    image_name = sanitize_filename(image_name)
                    filename = os.path.join(output_dir, f"{handle}_{image_name}")

                    with open(filename, "wb") as img_file:
                        img_file.write(response.content)

                    progress_bar.update(1)
                else:
                    print(f"[HTTP Error] {response.status_code} for handle: {handle}")
            except requests.exceptions.RequestException as e:
                print(f"[Request Error] for {handle}: {e}")
            except Exception as e:
                print(f"[File Error] for {handle}: {e}")

        progress_bar.close()
        print("Download completed.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    else:
        csv_path = "products_export.csv"  # default filename

    if not os.path.exists(csv_path):
        print(f"Error: CSV file '{csv_path}' not found.")
    else:
        download_images(csv_path)
