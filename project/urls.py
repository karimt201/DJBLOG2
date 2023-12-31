"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from posts.views import post_details , post_list,  create_post , edit_post , delete_post
from posts.views2 import postdetail , postlist , AddPost , EditPost , DeletePost
from posts.api import post_list_api , post_detail_api , PostListApi , PostDetailApi
from users.views import register , profile


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="BLOG API",
      default_version='v1',
      description="FULL BLOG API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', postlist.as_view(),name='home'),
    path('posts/new/', AddPost.as_view(),name='create_post') ,
    path('posts/<int:pk>/',postdetail.as_view(),name='post_detail'),
    path('posts/<int:pk>/edit/',EditPost.as_view(),name='Edit_post'),
    path('posts/<int:pk>/delete/',DeletePost.as_view(),name='Delete_post'),
    path('summernote/', include('django_summernote.urls')),
    path('register/', register,name='register'),
    path('profile/', profile,name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='logout'),







    path('posts/api' , PostListApi.as_view()) , 
    path('posts/api/<int:pk>' , PostDetailApi.as_view()) , 


    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''