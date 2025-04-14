from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bags/', views.bags, name='bags'),
    path('necklaces/', views.necklaces, name='necklaces'),
    path('shoes/', views.shoes, name='shoes'),
    path('appoint/', views.appoint, name='appoint'),
    path('kids/', views.kids, name='kids'),
    path('events/', views.events, name='events'),
    path('inquires/', views.inquires, name='inquires'),
    path('makeup/', views.makeup, name='makeup'),
    path('veils/', views.veils, name='veils'),
    path('earring/', views.earring, name='earring'),
    path('ceo/', views.ceo, name='ceo'),
    path('bracelets/', views.bracelets, name='bracelets'),
    path('evening/', views.evening, name='evening'),
    path('maid/', views.maid, name='maid'),
]