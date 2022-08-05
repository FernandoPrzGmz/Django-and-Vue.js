from django.urls import path

from src.apps.refugio import views

urlpatterns = [
    path('mascota/list/', views.MascotaListview.as_view(), name='mascota_list'),
    path('mascota/create/', views.MascotaCreateView.as_view(), name='mascota_create'),
    path('mascota/<slug:pk>/', views.MascotaDetailView.as_view(), name='mascota_detail'),
    path('mascota/<slug:pk>/update/', views.MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascota/<slug:pk>/delete/', views.MascotaDeleteView.as_view(), name='mascota_delete'),

    path('vue/', views.VueView.as_view(), name='vue'),
]