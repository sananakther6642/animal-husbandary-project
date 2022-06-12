"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from animal_husbandary.views import home, fo, stafflogin, userform, regform, feedbackform, feed, about, vaccination, product, order, staffdash, staffinfo, rform, ulog, stlog, search, msearch, vack, staffin, fd, uorder, coll,  cpass, getotp, changepass, deleteuser, delr
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),

    # path('vaccinat/', vaccinat),

    path('about/', about),
    path('stafflogin/', stafflogin),
    path('userform/', userform),
    path('regform/', regform),
    path('feedbackform/', feedbackform),
    path('feed/', feed),
    path('vaccination/', vaccination),
    path('product/', product),
    path('order/', order),
    path('staffdash/', staffdash),
    path('rform/', rform),
    path('ulog/', ulog),
    path('stlog/', stlog),
    path('search/', search),
    path('msearch/', msearch),
    path('vack/', vack),
    path('staffinfo/', staffinfo),
    path('staffin/', staffin),
    path('fd/', fd),
    path('coll/', coll),
    path('uorder/', uorder),


    path('fo/', fo),


    path('getotp/', getotp),
    path('cpass/', cpass),
    path('changepass/', changepass),
    path('deleteuser/', deleteuser),
    path('delr/', delr),




]
urlpatterns += staticfiles_urlpatterns()
