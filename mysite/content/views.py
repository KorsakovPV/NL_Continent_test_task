from rest_framework import viewsets

from content.models import ContentPageModel, ContentBaseMode
from content.serializers import ContentPageSerializer, ContentPageListSerializer
from rest_framework.response import Response

from content.tasks import content_count_increment


class PageViewSet(viewsets.ModelViewSet):
    queryset = ContentPageModel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        for content_obj in instance.content.all():
            if hasattr(content_obj, 'contentvideomodel'):
                obj_type = 'contentvideomodel'
            elif hasattr(content_obj, 'contentaudiomodel'):
                obj_type = 'contentaudiomodel'
            elif hasattr(content_obj, 'contenttextmodel'):
                obj_type = 'contenttextmodel'
            content_count_increment.delay(
                model_name=obj_type,
                obj_id=content_obj.id
            )
        return Response(serializer.data)


    def get_serializer_class(self):
        if self.request.user:
            if self.action in ['retrieve', ]:
                return ContentPageSerializer

        return ContentPageListSerializer
