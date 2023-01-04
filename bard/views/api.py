from api.database.mage import Mage
from flask import Blueprint, current_app, request, jsonify
from flask import Blueprint, request, jsonify
import logging

log = logging.getLogger(__name__)

blueprint = Blueprint("collections_api", __name__)


api = Blueprint("trip_reports_api", __name__)
log = logging.getLogger('werkzeug')


signals = [
    {
        'id': 181,
        'class': "first-class",
        'fare': 1200,
        'regID': 'abc',
        'results': [
            {
                'signalCount': 12,
                'regID': 'abc'
            },
            {
                'signalCount': 5,
                'regID': 'abc'
            },
            {
                'signalCount': 6,
                'regID': 'abd'
            }
        ]
    },
    {
        'id': 181,
        'class': "first-class",
        'fare': 1000,
        'regID': 'abc',
        'results': [
            {
                'signalCount': 12,
                'regID': 'abc'
            },
            {
                'signalCount': 5,
                'regID': 'abc'
            },
            {
                'signalCount': 6,
                'regID': 'abd'
            }
        ]
    },

    {
        'id': 181,
        'class': "second-class",
        'fare': 1000,
        'regID': 'abc',
        'results': [
            {
                'signalCount': 2,
                'regID': 'abee'
            },
            {
                'signalCount': 19,
                'regID': 'abc'
            },
            {
                'signalCount': 6,
                'regID': 'abd'
            }
        ]

    },
    {
        'id': 167,
        'class': "first-class",
        'fare': 1200,
        'regID': 'abcbb',
        'results': [
            {
                'signalCount': 12,
                'regID': 'abp'
            },
            {
                'signalCount': 5,
                'regID': 'abc'
            },
            {
                'signalCount': 1,
                'regID': 'abd'
            }
        ]
    },
    {
        'id': 181,
        'class': "second-class",
        'fare': 1500,
        'regID': 'abd',
        'results': [
            {
                'signalCount': 22,
                'regID': 'abc'
            },
            {
                'signalCount': 5,
                'regID': 'abcbb'
            },
            {
                'signalCount': 6,
                'regID': 'abd'
            }
        ]
    },
]


@api.route('/seed')
def seed_signals():
    collection = Mage()
    for document in signals:
        collection.insert_one(document)
    return "seed"


@api.route('/mages', methods=['POST'])
def create_collection():
    collection = Mage()
    document = {'document_1': 'delete_by_id'}
    collection.insert_one(document)
    return jsonify(document)


@blueprint.route("/", methods=["GET"])
def index():
    """
    List of collections
    """
    return "hello"


@api.route('/collections', methods=['GET'])
def fetch_magess():
    collection = Mage()
    collections = collection.find({})
    for collection in collections:
        collection['_id'] = str(collection['_id'])
    return collections


@blueprint.route("/create", methods=["POST", "PUT"])
def create():
    return "MTG Cards Update Here "
