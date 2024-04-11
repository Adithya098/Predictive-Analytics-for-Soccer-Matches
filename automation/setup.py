import requests
import os
import zipfile
import subprocess




def download_file(url, destination):
    """Download a file from a web URL to a local destination."""
    response = requests.get(url)
    if response.status_code == 200:
        # Open the destination file and write the contents of the response
        with open(destination, "wb") as file:
            file.write(response.content)
        print("Download completed successfully!")
    else:
        print("Failed to download file, status code:", response.status_code)
        
def check_folder_exists(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return True
    else:
        return False

def unzip_file(zip_path, extract_to=None):
    """Unzip a zip file.
    
    Args:
    zip_path (str): The path to the .zip file to extract.
    extract_to (str, optional): The directory to extract the files into. If not specified,
                                the files will be extracted into the same directory as the zip file.
    
    Returns:
    None
    """
    if extract_to is None:
        extract_to = os.path.dirname(zip_path)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Files extracted to: {extract_to}")


def main():
    print("install database file from this link: https://drive.google.com/file/d/12KGqHGtu-kQcwg6PEE2Qkst3KDQ1-khF/view?usp=share_link")
    input("Press any key to continue after downloading and place it in the working directory\n")

    if not check_folder_exists("betting_dataset"):   
        # URL for direct download
        download_url = "https://drive.google.com/uc?export=download&id=1AXvhfb6A3bY5E71uz3GW--toAKFlPJoe"

        # Local path where the file will be saved (update this to your desired path)
        save_path = "file.zip"

        # Download the file
        download_file(download_url, save_path)

        unzip_file("file.zip")

    subprocess.run("pip install -r requirements.txt", shell=True)
    
if __name__ == "__main__":
    main()

