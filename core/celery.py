from __future__ import absolute_import, unicode_literals

import celery


app = celery.Celery(include=['api.recommendations.tasks'])

app.config_from_object('core.settings', namespace="CELERY")
app.conf.update()
