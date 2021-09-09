from rest_framework import routers
from content.views import PageViewSet

router = routers.SimpleRouter()
# Client actions
router.register(r'page', PageViewSet)
urlpatterns = router.urls
