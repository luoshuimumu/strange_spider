import urllib.request

_max_num_retry=3

def download(url,num_retry=0):
    print('start download ',url,',num_retry=',num_retry)
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('download ',url,' error:',e.reason)
        html=None
        if(num_retry<=_max_num_retry):
            if hasattr(e,'code'):
                #  and (500<=e.code<600)):
                return download(url,num_retry+1)
    return html
# print(download('http://httpstat.us/500'))