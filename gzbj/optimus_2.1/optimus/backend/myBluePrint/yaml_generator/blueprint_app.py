from flask import Blueprint
from backend.myBluePrint.yaml_generator.api.v1.view import *

yaml_gen_bp = Blueprint('yaml_generator', __name__, url_prefix='/api/v1/config/yaml_gen')

yaml_gen_bp.add_url_rule('/', view_func=YamlGen.as_view('YamlGen'))
yaml_gen_bp.add_url_rule('/result', view_func=Result.as_view('Result'))
yaml_gen_bp.add_url_rule('/history', view_func=History.as_view('History'))

