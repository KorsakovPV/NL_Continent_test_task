import logging

from rest_framework.generics import get_object_or_404

from content.models import ContentVideoModel, ContentAudioModel, ContentTextModel
from mysite.celery import app

MODEL_TYPE = {
    'contentvideomodel': ContentVideoModel,
    'contentaudiomodel': ContentAudioModel,
    'contenttextmodel': ContentTextModel,
}


@app.task
def content_count_increment(model_name, obj_id):
    obj = get_object_or_404(MODEL_TYPE.get(model_name), id=obj_id)
    if hasattr(obj, 'counter'):
        obj.counter += 1
        obj.save()
    else:
        logging.warning(f"Объект {obj} не имеет атрибута counter")
