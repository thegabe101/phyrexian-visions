from bard.database.collections.mage import Mage
from flask import Blueprint, current_app, request, jsonify
from flask import Blueprint, request, jsonify
import logging

log = logging.getLogger(__name__)

blueprint = Blueprint("collections_api", __name__)

log = logging.getLogger('werkzeug')


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
    return "MTG Cards Update Here"
