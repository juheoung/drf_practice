from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('snippets', views.SnippetViewSet, basename='snippets')
urlpatterns = router.urls
