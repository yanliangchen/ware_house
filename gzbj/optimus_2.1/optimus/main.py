import sys
import argparse

sys.path.append('./celeryFolder')
from flask_cors import CORS
from mongoengine import connect as MONGO_CON
from config import MONGO_DBNAME, MONGO_HOST, MONGO_NAME, MONGO_PASS, MONGO_PORT, MONGO_TIMEOUT
from backend.scheduler_handler.scheduler_handler import SCHEDULER
# from werkzeug.routing import BaseConverter
from flask import Flask, render_template, request, make_response
from backend.param_check.sign_check import SignCheck, RefreshCheck, LoginCheck, LogoutCheck
from backend.customer.myCustomer import APiMethodView
from backend.service import LoginService, SignService, LogoutService, RefreshService
from backend.myBluePrint.yaml_generator.blueprint_app import yaml_gen_bp
from backend.myBluePrint.ericic_v2.blueprint_app import ericic_bp

# from backend.myBluePrint.ericic.blueprint_app import ericic_bp

app = Flask(
    __name__,
    static_folder='./frontend/static',
    template_folder='./frontend/templates',
)
# app.config.update(SECRET_KEY=b'_5!y2L"F4Q8z\n\xec]/', )

CORS(app, resources={r"/api/*": {"origins": "*"}})

URI = 'mongodb://{uname}:{pwd}@{host}:{port}/?authSource=admin'.format(uname=MONGO_NAME, pwd=MONGO_PASS,
                                                                       host=MONGO_HOST, port=MONGO_PORT)

MONGO_CON(MONGO_DBNAME, host=URI, serverSelectionTimeoutMS=MONGO_TIMEOUT, connectTimeoutMS=MONGO_TIMEOUT,
          socketTimeoutMS=MONGO_TIMEOUT)


# class RegexConverter(BaseConverter):
#     def __init__(self, url_map, *items):
#         super(RegexConverter, self).__init__(url_map)
#         self.regex = items[0]
#
# app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def index():
    return render_template('index.html'), 200


class Login(APiMethodView):
    check_cls = LoginCheck

    def post(self, *args, **kwargs):
        body = request.get_json()
        name = body.get('name')
        password = body.get('password')
        response = LoginService.authentication(name, password)
        return make_response(response), response['code']


class Sign(APiMethodView):
    check_cls = SignCheck

    def post(self, *args, **kwargs):
        body = request.get_json()
        name = body.get('name')
        password = body.get('password')
        res = SignService.sign_func(name, password)
        return res


class Logout(APiMethodView):
    check_cls = LogoutCheck

    def post(self, *args, **kwargs):
        body = request.get_json()
        refresh_token = body.get('refresh_token')
        res = LogoutService.logout_func(refresh_token)
        return res


class Refresh(APiMethodView):
    check_cls = RefreshCheck

    def post(self, *args, **kwargs):
        body = request.get_json()
        refresh_token = body.get('refresh_token')
        res = RefreshService.refresh_access_token(refresh_token)
        return res


# class Demo(APiMethodView):
#
#     def get(self, *args, **kwargs):
#         from celery_app import celery_app
#         # from script_executor.demo_func import demo_func
#         print('demo api start')
#         sync_switch = request.args.get('sync')
#         task = celery_app.send_task('script_executor.demo_func.demo_func', args=('job_id', 'admin',), task_id='job_id')
#
#         print(dir(task))
#         if sync_switch:
#             print()
#         else:
#             print()
#         print('demo api end')
#         return dict(status=True)


app.add_url_rule('/api/v2.1/login', view_func=Login.as_view('Login'))
app.add_url_rule('/api/v2.1/logout', view_func=Logout.as_view('Logout'))
app.add_url_rule('/api/v2.1/sign', view_func=Sign.as_view('Sign'))
app.add_url_rule('/api/v2.1/refresh', view_func=Refresh.as_view('Refresh'))
# app.add_url_rule('/demo', view_func=Demo.as_view('Demo'))

app.register_blueprint(yaml_gen_bp)
app.register_blueprint(ericic_bp)
SCHEDULER.scheduler.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-p", "--port", type=int, help="server port", default=8000)
    args = parser.parse_args()
    port = int(args.port)
    app.run(host='0.0.0.0', port=port, debug=False, threaded=False)
