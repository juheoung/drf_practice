from rest_framework import viewsets
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django_filters import rest_framework as filters


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class SnippetFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    startswith_title = filters.CharFilter(field_name='title', method='filter_startswith_title')

    def filter_startswith_title(self, queryset, name, value):
        title_filter = {f'{name}__startswith': value}
        return queryset.filter(**title_filter)

    class Meta:
        model = Snippet
        fields = ['title', 'code', 'price']


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # filter_backends = [filters.SearchFilter]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SnippetFilter

    def list(self, request, *args, **kwargs):
        print(request.user.username)

        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
