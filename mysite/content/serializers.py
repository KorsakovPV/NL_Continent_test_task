from rest_framework import serializers
from rest_framework.reverse import reverse

from content.models import ContentPageModel, ContentVideoModel, ContentAudioModel, ContentTextModel


class ContentVideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentVideoModel
        fields = '__all__'


class ContentAudioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentAudioModel
        fields = '__all__'


class ContentTextModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTextModel
        fields = '__all__'


class ContentBaseModeSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    page = serializers.UUIDField()
    counter = serializers.IntegerField()
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()
    # ContentVideoModel
    url_video = serializers.URLField(source='contentvideomodel.url_video', required=False)
    url_subtitles = serializers.URLField(source='contentvideomodel.url_subtitles', required=False)
    # ContentAudioModel
    bitrate = serializers.IntegerField(source='contentaudiomodel.bitrate', required=False)
    # ContentTextModel
    text = serializers.CharField(source='contenttextmodel.text', required=False)


class ContentPageSerializer(serializers.ModelSerializer):
    content = ContentBaseModeSerializer(many=True, read_only=True)

    class Meta:
        model = ContentPageModel
        fields = '__all__'


class ObjToLinkField(serializers.ReadOnlyField):

    def to_representation(self, value):
        return f"http://{self.context.get('request').get_host()}{reverse('contentpagemodel-detail', kwargs={'pk': value})}"


class ContentPageListSerializer(serializers.ModelSerializer):
    link = ObjToLinkField(source='id')

    class Meta:
        model = ContentPageModel
        fields = ('link',)
