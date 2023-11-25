from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
# from .permissions import IsOwner


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, ]  # IsOwner]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['status', 'created_at', ]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def get_permissions(self):  # на лекции мы предоставляли отдельно доступ для гет
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []
