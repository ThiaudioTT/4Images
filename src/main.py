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
    span_tags = soup.findAll("span", {"class": "file-info"}, recursive=True)

    # Print all tags
    for spanTag in span_tags: # WIP: spantag is empty
        print("TAG:", spanTag)



    return 0

if __name__ == "__main__":
    sys.exit(main())