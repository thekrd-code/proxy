import os, requests
from bs4 import BeautifulSoup

os.system("cls")
logo =r"""
  _____ _            _  ______  ____  
 |_   _| |__   ___  | |/ /  _ \|  _ \ 
   | | | '_ \ / _ \ | ' /| |_) | | | |
   | | | | | |  __/ | . \|  _ <| |_| |
   |_| |_| |_|\___| |_|\_\_| \_\____/ 
            t.me//anas_rasull
"""
print(logo)

def fetch_free_proxies():
    response = requests.get("https://www.free-proxy-list.net/")
    soup = BeautifulSoup(response.text, "html.parser")
    proxy_list = []

    table = soup.find("table", class_="table")

    for row in table.tbody.find_all("tr"):

        columns = row.find_all("td")

        ip = columns[0].text.strip()
        port = columns[1].text.strip()
        
        proxy = f"{ip}:{port}"
        proxy_list.append(proxy)

    return proxy_list


def write_proxies_to_file(proxies, filename="proxies.txt"):
    with open(filename, "w") as file:
        for proxy in proxies:
            file.write(proxy + "\n")


if __name__ == "__main__":

    print(". Getti proxies....")
    proxies = fetch_free_proxies()
    write_proxies_to_file(proxies)
    print(f"  {len(proxies)} proxy")
    input("\n  Enter Dabgra bo daxran...")

