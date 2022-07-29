import feedparser
channels = {
    'trang_chu': 'https://vnexpress.net/rss/tin-moi-nhat.rss', 
    'the_gioi': 'https://vnexpress.net/rss/the-gioi.rss', 
    'thoi_su': 'https://vnexpress.net/rss/thoi-su.rss', 
    'kinh_doanh': 'https://vnexpress.net/rss/kinh-doanh.rss', 
    'startup': 'https://vnexpress.net/rss/startup.rss', 
    'giai_tri': 'https://vnexpress.net/rss/giai-tri.rss', 
    'the_thao': 'https://vnexpress.net/rss/the-thao.rss', 
    'phap_luat': 'https://vnexpress.net/rss/phap-luat.rss', 
    'giao_duc': 'https://vnexpress.net/rss/giao-duc.rss', 
    'tin_moi_nhat': 'https://vnexpress.net/rss/tin-moi-nhat.rss', 
    'tin_noi_bat': 'https://vnexpress.net/rss/tin-noi-bat.rss', 
    'suc_khoe': 'https://vnexpress.net/rss/suc-khoe.rss', 
    'doi_song': 'https://vnexpress.net/rss/gia-dinh.rss', 
    'du_lich': 'https://vnexpress.net/rss/du-lich.rss', 
    'khoa_hoc': 'https://vnexpress.net/rss/khoa-hoc.rss', 
    'so_hoa': 'https://vnexpress.net/rss/so-hoa.rss', 
    'xe': 'https://vnexpress.net/rss/oto-xe-may.rss', 
    'y_kien': 'https://vnexpress.net/rss/y-kien.rss', 
    'tam_su': 'https://vnexpress.net/rss/tam-su.rss', 
    'cuoi': 'https://vnexpress.net/rss/cuoi.rss', 
    'tin_xem_nhieu': 'https://vnexpress.net/rss/tin-xem-nhieu.rss'
}
def parse(url):
    data = {}
    thefeed = feedparser.parse(url)
    '''print("Getting Feed Data")
    print(thefeed.feed.get("title", ""))
    print(thefeed.feed.get("link", ""))
    print(thefeed.feed.get("description", ""))
    print(thefeed.feed.get("published", ""))'''
    #count = len(thefeed.entries)
    for thefeedentry in thefeed.entries:
        title = thefeedentry.get("title", "")
        link = thefeedentry.get("link", "")
        data[link]=title
    return data
def get_articles(kenh):
    try:
        url = channels[kenh]
        data=parse(url)
        errors = False
    except KeyError:
        data = ""
        errors = False
    return data,errors

