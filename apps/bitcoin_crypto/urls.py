from django.conf.urls import url
from .views import IndexView, AboutView, IndexStatic, IndexSingle, ShortcodeWidgets, Services, ServicesSingle, \
    GalleryRegular, Timetable, ExchangeView, BlogRightView, ShopRightView


urlpatterns = [
    url(r'^index/', IndexView.as_view(), name='index'),
    url(r'^about/', AboutView.as_view(template_name='about.html'), name='about'),
    url(r'^index-static/', IndexStatic.as_view(), name='index_static'),
    url(r'^index-single/', IndexSingle.as_view(), name='index_single'),
    url(r'^shortcode-widgets/', ShortcodeWidgets.as_view(), name='shortcode_widgets'),
    url(r'^services/', Services.as_view(), name='services'),
    url(r'^services-single/', ServicesSingle.as_view(), name='services_single'),
    url(r'^gallery-regular/', GalleryRegular.as_view(), name='gallery_regular'),
    url(r'^timetable/', Timetable.as_view(), name='timetable'),
    url(r'^exchange/', ExchangeView.as_view(), name='exchange'),
    url(r'^blog-right/', BlogRightView.as_view(), name='blog_right'),
    url(r'^shop-right/', ShopRightView.as_view(), name='shop_right'),

]