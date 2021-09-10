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


class ContentPageSerializer(serializers.ModelSerializer):
    video = ContentVideoModelSerializer(many=True, read_only=True)
    audio = ContentAudioModelSerializer(many=True, read_only=True)
    text = ContentTextModelSerializer(many=True, read_only=True)

    class Meta:
        model = ContentPageModel
        fields = '__all__'


class ObjToLinkField(serializers.ReadOnlyField):

    # def __init__(self, **kwargs):
    #     kwargs['read_only'] = True
    #     super().__init__(**kwargs)

    def to_representation(self, value):
        return f"http://{self.context.get('request').get_host()}{reverse('contentpagemodel-detail', kwargs={'pk': value})}"


class ContentPageListSerializer(serializers.ModelSerializer):
    link = ObjToLinkField(source='id')

    class Meta:
        model = ContentPageModel
        fields = ('link',)
