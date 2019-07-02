from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from .models import GuideType, GuideDetail
from .serializers import GuideTypeSerializer, GuideDetailSerializer


class GuideTypeMsgs(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """获取指南分类信息"""
    # queryset = GuideType.objects.filter(guide_type=1)
    queryset = GuideTypeSerializer.setup_eager_loading(GuideType.objects.filter(guide_type=1))
    serializer_class = GuideTypeSerializer


class GuideDetailMsgs(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """获取详情信息"""
    # queryset = GuideDetail.objects.all()
    queryset = GuideDetailSerializer.setup_eager_loading(GuideDetail.objects.all())
    serializer_class = GuideDetailSerializer

    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('guide_type', )
