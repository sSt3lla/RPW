from flask import Blueprint
bp = Blueprint('auth', __name__, template_folder='Templates')
from ..auth import routes
                    