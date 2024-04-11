import requests

def download_file(url, target_path):
    # Send a GET request to the URL
    response = requests.get(url, stream=True)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file for writing in binary mode
        with open(target_path, 'wb') as out_file:
            # Write the contents of the response to the file in chunks
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    out_file.write(chunk)
        print("File downloaded successfully!")
    else:
        print("Failed to retrieve the file. Status code:", response.status_code)

if __name__ == "__main__":
    # Ensure the Dropbox URL ends with '?dl=1' to promote automatic downloads
    download_url = "https://docs.google.com/document/d/1YhV7scN75xdyCvy8u1LMhbuOpJcyhYJKPy8_I4gpfmw/export?format=doc"
    
    # Local path where the file will be saved
    save_path = "test.doc"
    
    # Download the file
    download_file(download_url, save_path)
