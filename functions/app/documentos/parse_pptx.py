from flask import jsonify, request
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import os  # Import the os module to work with file paths

from . import user_blueprint


@user_blueprint.route("/parse_pptx", methods=["POST"])
def parsear_pptx_handle():

    return jsonify(msg="Ok")
