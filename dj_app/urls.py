from django.conf.urls import url
from . import views

app_name = 'dj_app'
urlpatterns = [
    # ex: /dj_app/
    url(r'^$', views.index, name='index'),
    url(r'index.html$', views.index, name='index'),
    #url(r'php_publish.html$', views.get_jira_info),
    url(r'php_publish.html$', views.php_publish),
    url(r'net_publish.html$', views.net_publish),
    url(r'^create/', views.create_blogpost, name='create_blogpost'),
    url(r'^jira_info/',views.get_jira_info, name='get_jira_info'),
    url(r'^login.html', views.login, name='login'),
]
