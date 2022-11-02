from scrumboard.api import CardViewSet,ListViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'lists',ListViewSet)
router.register(r'lists',CardViewSet)

urlpatterns = router.urls