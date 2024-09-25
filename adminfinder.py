import requests
import threading
from fake_useragent import UserAgent

ua = UserAgent()  # To create random UserAgent for each request.

# Terminal colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

# To get total no. of lines in the file.
with open("path.txt", "r") as f:
    fileLen = len(f.readlines())


def print_banner():
  banner = f"""
{RED}:::::::::  :::       ::: ::::    :::       :::::::::     :::     ::::    ::: :::::::::: :::        
:+:    :+: :+:       :+: :+:+:   :+:       :+:    :+:  :+: :+:   :+:+:   :+: :+:        :+:        
+:+    +:+ +:+       +:+ :+:+:+  +:+       +:+    +:+ +:+   +:+  :+:+:+  +:+ +:+        +:+        
+#++:++#+  +#+  +:+  +#+ +#+ +:+ +#+       +#++:++#+ +#++:++#++: +#+ +:+ +#+ +#++:++#   +#+        
+#+        +#+ +#+#+ +#+ +#+  +#+#+#       +#+       +#+     +#+ +#+  +#+#+# +#+        +#+        
#+#         #+#+# #+#+#  #+#   #+#+#       #+#       #+#     #+# #+#   #+#+# #+#        #+#        
###          ###   ###   ###    ####       ###       ###     ### ###    #### ########## ########## 
{RESET}"""
  print(banner)

print_banner()

def checkURL(url):
    try:
        res = requests.get(url, headers={"User-Agent": ua.random}, timeout=5, )
        return res.status_code
    except Exception as e:
        # print(f"Error checking {url}: {e}")
        return None


def middleWare(url, baseURL):
    responseCode = checkURL(url)

    if responseCode == 200:
        print(GREEN+f"[200] - {url}"+RESET)
    else:
        print(RED+f"[{responseCode}] - {url}"+RESET)

    with open(f"{fileName}.txt", "a") as f:
        f.write(f"[{responseCode}] - {url}\n")


def createThread(totalThread, fileLen, url):
    start = 0
    differnce = fileLen // totalThread  # DIviding work for each Thread

    with open("path.txt", "r") as paths:
        lines = paths.readlines()

    threads = []
    for i in range(totalThread):
        end = start + differnce - 1 if i != totalThread - 1 else fileLen - 1
        sublist = lines[start:end+1]

        thread = threading.Thread(target=processURLs, args=(url, sublist))
        threads.append(thread)
        thread.start()

        start = end + 1

    for thread in threads:
        thread.join()


def processURLs(baseURL, paths):
    for path in paths:
        newURL = baseURL + "/" + path.strip("\n")  # Merge base URL with path
        middleWare(newURL, baseURL)


def adminFinder():
    url = input(
        f"{GREEN}[{RED}+{GREEN}]{RESET}{BLUE} Enter website URL: "+RESET).strip()
    totalThread = int(
        input(f"{GREEN}[{RED}+{GREEN}]{RESET}{BLUE} Enter number of threads: "+RESET))

    if not url.startswith("https://"):
        url = "https://" + url

    if checkURL(url) == 200:
        createThread(totalThread, fileLen, url)
    else:
        print(
            f"{GREEN}[{RED}-{GREEN}]{RESET}{RED} Website {url} is not accessible."+RESET)


if __name__ == "__main__":
    fileName = input(
        f"{GREEN}[{RED}+{GREEN}]{RESET}{BLUE} Enter file name [To store URL's]: "+RESET)
    adminFinder()
