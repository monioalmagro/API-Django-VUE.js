from rest_framework import routers

from .viewsets import BookviewSet

router = routers.SimpleRouter()
router.register('books', BookviewSet)

urlpatterns = router.urls
