from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
<<<<<<< HEAD
#from django.conf.urls.static import static

admin.autodiscover()
=======
from django.conf.urls.static import static

>>>>>>> 61b52e97ba020199e3f8bdea5faafc44491a0ee4
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ufpel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('ocupa.urls')),

<<<<<<< HEAD
)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 61b52e97ba020199e3f8bdea5faafc44491a0ee4
