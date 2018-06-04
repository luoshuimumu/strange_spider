def can_fetch(url,agent='GoodCrawler'):
    if 'badcrawler'==agent.lower():
        return False
    return True