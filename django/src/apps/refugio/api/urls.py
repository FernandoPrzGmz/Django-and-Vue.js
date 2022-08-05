from rest_framework import routers

from src.apps.refugio.api import views

router = routers.SimpleRouter()

router.register(r'vacunas', views.VacunaViewSet)
router.register(r'personas', views.PersonaViewSet)
router.register(r'mascotas', views.MascotaViewSet)

urlpatterns = []

urlpatterns += router.urls
