from flask import Blueprint

data = Blueprint('data', __name__, url_prefix='/api')

from . import routes  # noqa: F401 E402
