from models import Advertiser
from models.ad import Ad

if __name__ == '__main__':
    advertiser1 = Advertiser('name1')
    advertiser2 = Advertiser('name2')
    ad1 = Ad(title='title1', image_url='image-url1', link='link1', advertiser=advertiser1)
    ad2 = Ad(title='title2', image_url='image-url2', link='link2', advertiser=advertiser2)
    ad2.describe_me()
    advertiser1.describe_me()
    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad2.inc_views()
    ad1.inc_clicks()
    ad1.inc_clicks()
    ad2.inc_clicks()
    print(advertiser2.get_name())
    advertiser2.set_name('new name')
    print(advertiser2.get_name())
    print(ad1.get_clicks())
    print(advertiser2.get_clicks())
    print(Advertiser.get_total_clicks())
    print(Advertiser.help())