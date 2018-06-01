import re


def crawl_sitemap(url):
    sitemap = open(url).read()
    pattern = re.compile('[href="](.*)[">]')
    links = pattern.findall(sitemap)
    for link in links:
        print(link)
