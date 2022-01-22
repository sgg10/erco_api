from flask import Blueprint

from . import routes  # noqa: F401

data = Blueprint('data', __name__, url_prefix='/api')
