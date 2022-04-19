"""NittanyMarket URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
]

admin.site.site_header = 'Nittany Market Admin'                    # default: "Django Administration"
admin.site.index_title = 'Nittany Market Site Administration'                 # default: "Site administration"
admin.site.site_title = 'Nittany Market site admin'  # default: "Django site admin"

if settings.DEBUG:  # in debug mode, uses the media folder in the root directory to store uploaded media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
