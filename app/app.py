from flask_restx import Resource, Api
from models import app

api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host='0.0.0.0')
    app.run(debug=True)
