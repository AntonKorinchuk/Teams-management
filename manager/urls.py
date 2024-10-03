from rest_framework.routers import DefaultRouter

from manager.views import TeamViewSet, PersonViewSet


router = DefaultRouter()
router.register("teams", TeamViewSet)
router.register("persons", PersonViewSet)

urlpatterns = router.urls

app_name = "manager"
