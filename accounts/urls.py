from django.urls import path

from accounts.views import *
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', index, name='index'),

    # get article by article id at 127.0.0.1/article/id
    path('article/<int:id>/', get_article_by_id, name='get_article_by_id'),

    # search article(s) by text at 127.0.0.1/search/text
    path('search/<str:text>', search_by_article_text, name='search_text'),

    # all articles archive at 127.0.0.1/archive
    path('archive/', articles_archive, name='archive'),

    path('user/<int:id>/', get_user_by_id, name='get_user_by_id')
]

app_name = 'accounts' # using namespace

