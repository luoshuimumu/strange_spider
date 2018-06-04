class throttle:
    """限速，规定时间内只允许爬取一次
    """
    def __init__(self,delay):
        self.delay=delay
        self.domain={}

    def wait(self,url):
        # domain=urlparse(url).netloc
        return