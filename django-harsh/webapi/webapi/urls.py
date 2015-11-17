from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [

    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('jackpot.urls')),

    # Examples:
    # url(r'^$', 'webapi.views.home', name='home'),
    # url(r'^webapi/', include('webapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    

    #user auth urls
    #url(r'^accounts/login/$', 'webapi.views.login'),
    #url(r'^accounts/auth/$', 'webapi.views.auth_views'),
    #url(r'^accounts/logout/$', 'webapi.views.logout'),
    #url(r'^accounts/loggedin/$', 'webapi.views.loggedin'),
    #url(r'^accounts/invalid/$', 'webapi.views.invalid_login'),
    #url(r'^accounts/register/$', 'webapi.views.register_user'),
    #url(r'^accounts/register_success/$', 'webapi.views.register_success'),

]
