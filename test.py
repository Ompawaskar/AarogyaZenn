import requests
import os
import yogadata

def download_image(url, filepath):
    """
    Downloads an image from the given URL and saves it to the specified file path.
    Handles potential errors and ensures file path validity.
    """

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Ensure the desired directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Image saved to: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")

# Example usage:
for i in yogadata.data:
    p = os.getcwd()
    p1 = "yimages"
    p3 = str(i['id'])+".png"
    path = os.path.join(p,p1,p3)
    image = i['url_png']
    download_image(image,path)