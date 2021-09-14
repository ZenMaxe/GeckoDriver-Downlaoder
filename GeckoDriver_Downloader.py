""""
===============]ZenMaxe[===============
| ZenMaxe Geckodriver Downloader v0.1 |
|            No Copyright             |
|         Give Star On GitHub         |
=======================================
"""




#import Libraries
import requests
import os

from bs4 import BeautifulSoup
def download_geckodriver(version, geckodriver_link):
    if os.name == 'nt':
        #Working on Windows Version 
        pass    
    
    else:
        path = os.path.dirname(__file__)
        geckodriver_linux = f"https://github.com/mozilla/geckodriver/releases/download/{version}/geckodriver-{version}-linux64.tar.gz"
        #Download GeckoDriver with Wget command
        os.system(f"wget {geckodriver_linux}")
        #untar geckodriver 
        os.system(f"sudo tar -xvf ./geckodriver-{version}-linux64.tar.gz")
        #make executable
        os.system(f"sudo chmod +x geckodriver")
        #add to path for selenium or you can enter geckodriver path manually on your selenium script
        os.system(f"export PATH=$PATH:/{path}/geckodrive")

        

def main():
    #get lastet version
    geckodriver_link = "https://github.com/mozilla/geckodriver/releases/latest"
    req = requests.get(geckodriver_link)
    soup = BeautifulSoup(req.content, 'html.parser')
    job_elements = soup.find("span",style="max-width: 125px" ).getText()
    version = job_elements
    
    download_geckodriver(version , geckodriver_link)



if __name__ == '__main__':
    main()