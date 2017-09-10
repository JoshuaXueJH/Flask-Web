from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


# inject Permission to context, if not, will get an error of "UndefinedError: 'Permission' is undefined"
@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)
