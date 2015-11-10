from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.flatpages import views

import events.views
import users.views
import projects.views
from incubator import settings
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern



router = routers.DefaultRouter()
router.register(r'events', events.views.EventViewSet)
router.register(r'users', users.views.UserViewSet)
router.register(r'projects', projects.views.ProjectViewSet)


urlpatterns = patterns(
    '',
    url(r'^$', 'incubator.views.home', name='home'),
    url(r'^events/', include('events.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^accounts/', include('users.urls')),
    url(r'^space/', include('space.urls')),

    url(r'^sm', 'events.views.sm'),
    url(r'^linux', 'events.views.linux'),
    url(r'^git', 'events.views.git'),
    url(r'^ag', 'events.views.ag'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/',

    ), name="register"),

    url(r'^api/', include(router.urls)),
    (r'^notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern()),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
