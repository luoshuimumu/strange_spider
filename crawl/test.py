from link_crawler import link_crawler
from download import download
from urllib.parse import urljoin

#print(download('http://fecipher.card.moe/'))
print(link_crawler('http://fecipher.card.moe/Package.aspx','/Package/.*aspx'))

# print(urljoin())