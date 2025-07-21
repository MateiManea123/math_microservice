
from flask import Flask, jsonify, request, Blueprint, make_response,abort

from app.functions import *
from app.models import *
from app.monitor import *


bp = Blueprint('math_routes', __name__)


@bp.errorhandler(400)
def handle_400_error(error):
    return make_response(jsonify({'error': error.description}), 400)
@bp.errorhandler(404)
def handle_404_error(error):
    return make_response(jsonify({'error': error.description}),404)
@bp.errorhandler(500)
def handle_500_error(error):
    return make_response(jsonify({'error': error.description}),500)



@bp.route("/pow", methods=['POST'])
def pow_function():
    print_usages()
    add_request(request)
    data = request.get_json()
    number = data.get('number')
    if not isinstance(number,(int,float)) or number<0:
        abort(400,description="Your input should be a positive number!")
    power = data.get('pow')

    log_event("POST request on /pow", {"input": [number,power]}
              )

    if not isinstance(power,(int,float)) or power<0:
        abort(400,description="Your input should be a number!")
    number = poww(number,power)
    return jsonify(number)

@bp.route("/fibonacci", methods=['POST'])
def post_fibonacci():
    print_usages()
    add_request(request)
    data= request.get_json()
    n = data.get('n')
    log_event("POST request on /fibonacci", {"input": n})
    if not isinstance(n,int) or n<0:
        abort(400,description="Your input should be a positive integer number!")
    res = nth_fibonacci(n)
    return jsonify(res)


@bp.route("/factorial", methods=['POST'])
def post_factorial():

    print("ALOOO")
    add_request(request)
    data=request.get_json()
    n=data.get('n')

    log_event("POST request on /factorial", {"input": n})


    if not isinstance(n,int) or n<=0:
        abort(400,description="Your input should be a positive integer number!")
    res = factorial(n)
    return jsonify(res)




@bp.route("/requests", methods=['GET'])
def get_requests():
    log_event("GET request on /requests")
    request_dict = {}
    requests = Request.query.all()
    for req in requests:
        request_dict[req.id] =  {"method": req.method, "headers": req.headers, "body" : req.body }
    return jsonify(request_dict)

