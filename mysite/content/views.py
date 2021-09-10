from rest_framework import viewsets

from content.models import ContentPageModel
from content.serializers import ContentPageSerializer, ContentPageListSerializer
from rest_framework.response import Response

from content.tasks import content_count_increment


class PageViewSet(viewsets.ModelViewSet):
    queryset = ContentPageModel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        for contents in [
            instance.video.all(),
            instance.audio.all(),
            instance.text.all()
        ]:
            for content_obj in contents:
                content_count_increment.delay(
                    model_name=getattr(content_obj, '_meta').model_name,
                    obj_id=content_obj.id
                )
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.user:
            if self.action in ['retrieve', ]:
                return ContentPageSerializer

        return ContentPageListSerializer
