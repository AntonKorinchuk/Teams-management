from rest_framework.routers import DefaultRouter

from views import TeamViewSet, PeopleViewSet


router = DefaultRouter()
router.register("teams", TeamViewSet)
router.register("peoples", PeopleViewSet)

urlpatterns = router.urls

app_name = "manager"
