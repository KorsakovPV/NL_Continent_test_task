from django.contrib import admin

from content.models import ContentPageModel, ContentVideoModel, ContentAudioModel, ContentTextModel


class TimeStampedModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')


class ContentVideoModelLineAdmin(admin.TabularInline):
    model = ContentVideoModel


class ContentAudioModelLineAdmin(admin.TabularInline):
    model = ContentAudioModel


class ContentTextModelLineAdmin(admin.TabularInline):
    model = ContentTextModel


@admin.register(ContentPageModel)
class ContentPageModelAdmin(TimeStampedModelAdmin):
    search_fields = ('title', 'video__title', 'audio__title', 'text__title')
    inlines = [
        ContentVideoModelLineAdmin, ContentAudioModelLineAdmin, ContentTextModelLineAdmin,
    ]


@admin.register(ContentVideoModel)
class ContentVideoModelAdmin(TimeStampedModelAdmin):
    search_fields = ('title',)


@admin.register(ContentAudioModel)
class ContentAudioModelAdmin(TimeStampedModelAdmin):
    search_fields = ('title',)


@admin.register(ContentTextModel)
class ContentTextModelAdmin(TimeStampedModelAdmin):
    search_fields = ('title',)
