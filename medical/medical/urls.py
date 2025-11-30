"""
URL configuration for medical project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from meditrust import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',views.Register,name='reg'),
    path('',views.home,name='h'),
    path('login/',views.login,name='login'),
    path('aboutus/',views.aboutus,name='au'),
    path('contact/',views.contact,name='cus'),
    path('admin1/',views.admin12,name='ad'),
    path('totalsales/',views.totalsales,name='ts'),
    path('datewise/',views.datewise,name='sdw'),
    path('operatorwise/',views.operatorwise,name='sow'),
    path('addoper/',views.addoper,name='ao'),
    path('date/',views.singledate,name='sd'),
    path('deleteop/',views.deleteoper,name='do'),
    path('main/',views.main,name='main'),
    path('addm/',views.addm,name='am'),
    path('removem/',views.removem,name='rm'),
    path('searchm/',views.searchm,name='sm'),
    path('billing/',views.billingm,name='bm'),
    path('checkamt/',views.checkm,name='chk'),
    path('operator',views.operator,name='oper'),
    path('midadd/',views.midadd,name='ma'),
    path('update/',views.updatemid,name='un'),
    path('alogin/',views.alogin,name='al')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
