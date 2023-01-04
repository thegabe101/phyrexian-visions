from flask import Blueprint, request, jsonify
import logging

log = logging.getLogger(__name__)

blueprint = Blueprint("collections_api", __name__)

@blueprint.route("/", methods=["GET"])
def index():
    """
    List of collections
    """
    return "hello"

@blueprint.route("/create", methods=["POST", "PUT"])
def create():
    return "not hot reloaddf dfad "
