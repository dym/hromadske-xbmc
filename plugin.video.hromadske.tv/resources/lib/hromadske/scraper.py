import urllib2
from BeautifulSoup  import BeautifulSoup
from xbmcswift2 import Plugin


CHANNEL_URL = 'http://www.youtube.com/user/HromadskeTV'
plugin = Plugin()


def get_url(url):
    post = None
    html = ''
    request = urllib2.Request(url)

    request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)')

    try:
        f = urllib2.urlopen(request)
        html = f.read()
    except IOError, e:
        if hasattr(e, 'reason'):
            plugin.log.error('We failed to reach a server. Reason: {}'.format(e.reason))
        elif hasattr(e, 'code'):
            plugin.log.error('The server couldn\'t fulfill the request. Error code: {}'.format(str(e.code)))

    return html


def get_online_video_id():
    video_id = None
    html = get_url(CHANNEL_URL)
    if html:
        soup = BeautifulSoup(html)
        rec = soup.find('ul', {'class': 'yt-uix-slider-list'}).find('li').find('button')
        if rec:
            video_id = rec['data-video-ids']

    return video_id
