from django.contrib import admin
from django.urls import path
from quran.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surah/<int:surah_number>/<int:verse_number>/<str:translator_id>/<str:reader_id>/<str:purchased>/<int:usage_count>/', verse_view),
    path('surah/<int:surah_number>/<int:verse_number>/<str:translator_id>/<str:reader_id>/<int:usage_count>/', verse_view),
    path('surah/<int:surah_number>/<str:purchased>/<int:usage_count>/', verse_view),
    path('surah/<int:surah_number>/<int:usage_count>/', verse_view),
    path('surah/<str:purchased>/<int:usage_count>/', surah_view),
    path('surah/<int:usage_count>/', surah_view),
    path('buy/<int:usage_count>/', buy_view),
    path('<str:purchased>/<int:usage_count>/', main_view),
    path('<int:usage_count>/', main_view),
    path('', main_view),
]

