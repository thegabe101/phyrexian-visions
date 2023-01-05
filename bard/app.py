import logging
from flask import Flask, request

from bard import settings

NONE = "'none'"
log = logging.getLogger(__name__)
from bard.database.mongo.mongodb_conn import MongoDBConn

def create_app(config={}):

    app = Flask("bard")
    app.config.from_object(config)
    app.config.update(config)

    from bard.views import mount_app_blueprints

    mount_app_blueprints(app)
    return app

