import datetime
import re
import requests

from bs4 import BeautifulSoup
import pandas as pd 
import proxy

"""
Chrome:
  accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
  accept-encoding: gzip, deflate, br
  accept-language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
  cache-control: max-age=0
  sec-fetch-dest: document
  sec-fetch-mode: navigate
  sec-fetch-site: same-origin
  sec-fetch-user: "?1"
  upgrade-insecure-requests: "1"
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Edge:
  accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
  accept-encoding: gzip, deflate, br
  accept-language: en-GB,en;q=0.9,en-US;q=0.8
  cache-control: max-age=0
  sec-fetch-dest: document
  sec-fetch-mode: navigate
  sec-fetch-site: none
  sec-fetch-user: "?1"
  upgrade-insecure-requests: "1"
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44
Firefox:
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
  Accept-Encoding: gzip, deflate, br
  Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
  Connection: keep-alive
  DNT: "1"
  Upgrade-Insecure-Requests: "1"
  Sec-Fetch-Dest: document
  Sec-Fetch-Mode: navigate
  Sec-Fetch-Site: cross-site
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0
IE:
  Accept: text/html, application/xhtml+xml, image/jxr, */*
  Accept-Encoding: gzip, deflate
  Accept-Language: en-GB
  Connection: Keep-Alive
  User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
"""

### Fetch the proxies IP @
def get_proxies_url():
    res = requests.get("https://free-proxy-list.net/")
    proxy_list = pd.read_html(res.text)[0]
    proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)
    return proxy_list

url = "https://www.france-pari.fr/football/france/ligue-1-uber-eats-r"
#url = "https://httpbin.org/user-agent"
https_proxies = get_proxies_url()
print(https_proxies)

#soup = BeautifulSoup(requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}).content, features="lxml")
#print(soup)