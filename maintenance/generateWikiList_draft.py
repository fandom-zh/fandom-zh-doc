from bs4 import BeautifulSoup
import re
import requests

languages = {
  "zh": "zh",
  "zh-hk": "zh-hk",
  "zh-tw": "zh-tw"
}

for key, value in languages:
  r = requests.get("http://community.fandom.com/wiki/Special:Newwikis?start=&language=" + key + "&limit=5000")
  soup = BeautifulSoup(r.content, "html.parser")
  rawHTML = soup.select_one('#mw-content-text .mw-spcontent ul')
  csvData = re.sub(r'<li>\n	<a href="http:\/\/([^"]*)\/">([^<]*)<\/a>\n			\(([^,]*),  ([^	]*)		Founder name: <a href="https:\/\/community\.fandom\.com\/wiki\/Special:CheckUser\?user=[^"]*">([^<]*)<\/a>\n		, Email: <a href="https:\/\/community\.fandom\.com\/wiki\/Special:LookupUser\?target=[^"]*">[^<]*<\/a>\n		, Confirm: [^	](	)*(, IP: <a href="https:\/\/community\.fandom\.com\/wiki\/Special:MultiLookup\?target=[^"]*">[^<]*<\/a>\)\n			)*<\/li>', '"","https://$1","$2","$3","$4","$5","","",""', rawHTML)
  print(csvData)
