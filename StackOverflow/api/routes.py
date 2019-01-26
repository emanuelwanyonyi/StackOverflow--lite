from flask import Blueprint

blueprint = Blueprint('api', __name__)

@blueprint.route('/getStuff')
def getStuff():
    return '{"result" : "You are in the API!!"}'