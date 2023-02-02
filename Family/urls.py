
from django.contrib import admin
from django.urls import path
from myfamily import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('personapi/',views.person_api,name='personapi'),
    path('personapi/<int:pk>/',views.person_api,name='personapi'),
    path('grandfatherapi/',views.grandfather_api,name='grandfatherapi'),
    path('grandfatherapi/<int:pk>/',views.grandfather_api,name='grandfatherapi'),
    path('grandmotherapi/',views.grandmother_api,name='grandmotherapi'),
    path('grandmotherapi/<int:pk>/',views.grandmother_api,name='grandmotherapi'),
    path('fatherapi/',views.father_api,name='fatherapi'),
    path('fatherapi/<int:pk>/',views.father_api,name='fatherapi'),
    path('motherapi/',views.mother_api,name='motherapi'),
    path('motherapi/<int:pk>/',views.mother_api,name='motherapi'),
    path('sonapi/',views.son_api,name='sonapi'),
    path('sonapi/<int:pk>/',views.son_api,name='sonapi'),
    path('daughterapi/',views.daughter_api,name='daughterapi'),
    path('daughterapi/<int:pk>/',views.daughter_api,name='daughterapi'),
         
    path('tree/<int:pk>/',views.getfamily)
]
