from flask import Blueprint, request, jsonify

from Controllers.ControllerValidator import validate_score_request, validate_ai_request
from Modules.AIModule import AIModule
from Modules.ScoreModule import ScoreModule

main_routes = Blueprint('main', __name__)
ai_module = AIModule()

@main_routes.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    if not validate_score_request(data):
        return jsonify({'error': 'Invalid request'}), 400
    board = data['board']
    piece = data['piece']
    position = data['position']
    return jsonify({'score': ScoreModule.get_action(board, position, piece)})


@main_routes.route('/ai', methods=['POST'])
def ai():
    data = request.get_json()
    if not validate_ai_request(data):
        return jsonify({'error': 'Invalid request'}), 400
    board = data['board']
    piece = data['piece']
    max_depth = data['max_depth']
    method = data['method']
    return jsonify({'position': ai_module.get_action(board, piece, max_depth, method)})

@main_routes.route('/tree', methods=['GET'])
def tree():
    return jsonify({'tree': ai_module.get_root().to_dict()})