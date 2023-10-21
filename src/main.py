import sys
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    # zipFile = True # for future use

    if len(sys.argv) < 2:
        print("Couldn't find the website argument")
        sys.exit(1)
    
    url = sys.argv[1]

    # Todo : validate website
    print("THREAD: ", url)

    response = requests.get(url)
    if response.status_code != 200:
        print("Couldn't get the website")
        sys.exit(1)
    
    # GET all posts
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.select("body.is_thread > #delform > div.board > div.thread")
    posts = posts[0].select("div.postContainer")

    # Create folder to save images
    FOLDER_NAME = "downloaded_images"
    os.makedirs(FOLDER_NAME, exist_ok=True)

    imagesDownloaded = 0

    # Do the main work, donwload images and save them
    for index, post in enumerate(posts): # TODO: verifies if this is the best efficient way to do it
        fileLinkTag = post.select_one("div.post > div.file > div.fileText > a")

        print("Post:", index + 1, "FileTag:", fileLinkTag, " ")

        if fileLinkTag:
            imageURL = "https:" + fileLinkTag['href']

            print("Downloading from: ", imageURL, "\n")
            img = requests.get(imageURL)
            if img.status_code == 200:
                with open(os.path.join(FOLDER_NAME, imageURL.split('/')[-1]), 'wb') as f:
                    f.write(img.content)
                    f.close()
                imagesDownloaded += 1
            else:
                print("!!!Couldn't get the image from: ", imageURL, "\n")

    # Success message
    print("Done!\nDownloaded", imagesDownloaded, "images in", FOLDER_NAME, "folder")

    return 0

if __name__ == "__main__":
    sys.exit(main())