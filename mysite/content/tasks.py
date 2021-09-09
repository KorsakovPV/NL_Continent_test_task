import logging

from mysite.celery import app


@app.task
def content_count_increment(obj):
    if hasattr(obj, 'counter'):
        obj.counter += 1
        obj.save()
    else:
        logging.warning(f"Объект {obj} не имеет атрибута counter")
