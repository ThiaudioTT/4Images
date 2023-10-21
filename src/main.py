import sys
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    zipFile = True # for future use

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
    
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all images in span
    # span_tags = soup.findAll("span", {"class": "file-info"}, recursive=True)
    posts = soup.select("body.is_thread > #delform > div.board > div.thread")
    # posts = soup.find_all("body.is_thread > #delform > div.board > div.thread > postContainer")
    posts = posts[0].select("div.postContainer")

    # print(spanTag)

    # Skip first post
    # OpPost = posts[0] # Verify if is deep copy
    # posts = posts[1:]

    # Print all files link
    for post in posts:
        fileLinkTag = post.select_one("div.post > div.file > div.fileText > a")
        # print with a new line

        print("FileTag: ", fileLinkTag, " ")

        if fileLinkTag:
            print("FileLinkTag: ", fileLinkTag['href'], "\n")



    return 0

if __name__ == "__main__":
    sys.exit(main())