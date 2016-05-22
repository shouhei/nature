from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://d.hatena.ne.jp/naoya/")
with urlopen("http://d.hatena.ne.jp/naoya/") as response:
   html = response.read()
   soup = BeautifulSoup(html, "html.parser")
   body = soup.body
   if soup.script is not None:
       for s in soup.find_all("script"):
           s.decompose()
   if soup.noscript is not None:
       for n in soup.find_all("noscript"):
           n.decompose()
   if soup.style is not None:
       for s in soup.find_all("style"):
           s.decompose()
   print(body.get_text())
