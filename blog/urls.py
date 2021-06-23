
from django.urls import path,include
app_name = 'blog'
from . import views
urlpatterns = [
    path('',views.bloghome,name="bloghome"),
path('<int:blog_id>/',views.detail,name="detail"),
]