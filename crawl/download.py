import urllib.request

def download(url,num_retry=2):
    print('start download')
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('download ',url,' error:',e.reason)
        html=None
        if(num_retry>0):
            if(hasattr(e,'code') and (500<=e.code<600)):
                return download(url,num_retry-1)
    return html
# print(download('http://httpstat.us/500'))