from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'code']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
