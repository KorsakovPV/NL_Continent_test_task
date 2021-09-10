import uuid

from django.db import models
from model_utils.models import TimeStampedModel


class ContentBaseMode(TimeStampedModel):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField('Title', max_length=1000)

    class Meta:
        abstract = True


class ContentWithCounterBaseMode(ContentBaseMode):
    counter = models.IntegerField('Counter', default=0)

    class Meta:
        abstract = True
        ordering = ('created',)


class ContentPageModel(ContentBaseMode):
    pass

    class Meta:
        verbose_name = 'Content page'
        verbose_name_plural = 'Content pages'


class ContentVideoModel(ContentWithCounterBaseMode):
    page = models.ForeignKey(
        ContentPageModel, verbose_name='Page', on_delete=models.PROTECT,
        related_name='video'
    )
    url_video = models.URLField('Video URL', blank=True)
    url_subtitles = models.URLField('Subtitles URL', blank=True)

    class Meta:
        verbose_name = 'Content video'
        verbose_name_plural = 'Content videos'


class ContentAudioModel(ContentWithCounterBaseMode):
    page = models.ForeignKey(
        ContentPageModel, verbose_name='Page', on_delete=models.PROTECT,
        related_name='audio'
    )
    bitrate = models.IntegerField('Bitrate', null=True, default=None)

    class Meta:
        verbose_name = 'Content audio'
        verbose_name_plural = 'Content audios'


class ContentTextModel(ContentWithCounterBaseMode):
    page = models.ForeignKey(
        ContentPageModel, verbose_name='Page', on_delete=models.PROTECT,
        related_name='text'
    )
    text = models.TextField('Text')

    class Meta:
        verbose_name = 'Content text'
        verbose_name_plural = 'Content texts'
