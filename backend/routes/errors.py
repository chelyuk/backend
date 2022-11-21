import traceback

from flask import Blueprint, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

error_bp = Blueprint("errors", __name__)


@error_bp.app_errorhandler(ValidationError)
def handle_invalid_data(error):
    print(traceback.format_exc())
    return jsonify({"message": "Incorrect format data"}), 400


@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return jsonify({"message": "This resourse isn't available"}), 404


@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
    return jsonify({"message": "Unknown error. Please check the logs for more details"}), 500
