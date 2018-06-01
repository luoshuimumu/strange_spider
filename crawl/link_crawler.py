import re
from download import download
from urllib.parse import urljoin 

def link_crawler(seed_url,link_regex):
    crawl_queue=[seed_url]
    result=[]
    seen=set(crawl_queue)
    while crawl_queue:
        url=crawl_queue.pop()
        html=download(url)
        if None!=html:
            html=html.decode('utf-8')
        pattern=re.compile(link_regex)
        for link in get_links(html):
            if pattern.match(link):
                link=urljoin(seed_url,link)
                if(link not in seen):
                    crawl_queue.append(link)
                    result.append(link)
    return result
            
#正则匹配<href>
def get_links(html):
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']')
    #(Package)\S*aspx
    #<a[^>]+href=["\'](.*?)["\']
    return webpage_regex.findall(html)