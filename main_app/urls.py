from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boats/', views.boats_index, name='index'),
    path('boats/<int:boat_id>/', views.boats_detail, name='detail'),
    path('boats/create', views.BoatCreate.as_view(), name='boat_create'),
    path('boats/<int:pk>/update/', views.BoatUpdate.as_view(), name='boat_update'),
    path('boats/<int:pk>/delete/', views.BoatDelete.as_view(), name='boat_delete'),
    path('boats/<int:boat_id>/add_service/', views.add_service, name='add_service'),
    path('parts/', views.PartList.as_view(), name='parts_index'),
    path('parts/<int:pk>/', views.PartDetail.as_view(), name='parts_detail'),
    path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    path('parts/<int:pk>/update/', views.PartUpdate.as_view(), name='parts_update'),
    path('parts/<int:pk>/delete/', views.PartDelete.as_view(), name='parts_delete'),
    path('boats/<int:boat_id>/assoc_part/<int:part_id>/', views.assoc_part, name='assoc_part'),path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    path('accounts/signup', views.signup, name='signup'),
]