import uuid

from django.db import models
from model_utils.models import TimeStampedModel


class BaseMode(TimeStampedModel):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField('Title', max_length=1000)

    class Meta:
        abstract = True


class ContentPageModel(BaseMode):
    pass

    class Meta:
        verbose_name = 'Content page'
        verbose_name_plural = 'Content pages'


class ContentBaseMode(BaseMode):
    page = models.ForeignKey(
        ContentPageModel, verbose_name='Page', on_delete=models.PROTECT,
        related_name='content'
    )
    counter = models.IntegerField('Counter', default=0)

    class Meta:
        ordering = ('created',)


class ContentVideoModel(ContentBaseMode):
    url_video = models.URLField('Video URL', blank=True)
    url_subtitles = models.URLField('Subtitles URL', blank=True)

    class Meta:
        verbose_name = 'Content video'
        verbose_name_plural = 'Content videos'


class ContentAudioModel(ContentBaseMode):
    bitrate = models.IntegerField('Bitrate', null=True, default=None)

    class Meta:
        verbose_name = 'Content audio'
        verbose_name_plural = 'Content audios'


class ContentTextModel(ContentBaseMode):
    text = models.TextField('Text')

    class Meta:
        verbose_name = 'Content text'
        verbose_name_plural = 'Content texts'
