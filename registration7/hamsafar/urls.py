from django .urls import path
from . import views
urlpatterns=[
    path('k/',views.create,name="create"),
    path('',views.login,name="login"),
    path('kk/',views.home,name="home"),
    path('kkk/',views.logout,name="logout"),
]