import traceback

from flask import Blueprint, request, jsonify

# Models
from src.models.UserModel import User
# Services
from src.services.UserService import UserService
# Logger
from src.utils.Logger import Logger
# Security
from src.utils.Security import Security

main = Blueprint('user_blueprint', __name__)


@main.route('/')
def find():
    try:
        id = request.json['id']

        if id is None:
            response = jsonify({
                'success': False,
                "response": "user id is required"}
            )
            return response, 401

        _user = User(id, None, None, None)
        user_db = UserService.find(_user)
        print(user_db)

        response = jsonify({
            'success': True,
            "response": jsonify(User(*user_db).to_dict())
        })
        return response, 200

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})


@main.route('/', methods=['POST'])
def create():
    try:
        username = request.json['username']
        password = request.json['password']
        full_name = request.json['fullName']

        new_user = User(None, username, password, full_name)
        res = UserService.save(new_user)

        response = jsonify({
            'success': True,
            "response": res}
        )
        return response, 200

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})


@main.route('/', methods=['PUT'])
def update():
    try:
        id = request.json['id']
        username = request.json['username']
        password = request.json['password']
        full_name = request.json['fullName']

        if id is None:
            response = jsonify({
                'success': False,
                "response": "user id is required"}
            )
            return response, 401

        _user = User(id, username, password, full_name)
        UserService.update(_user)

        response = jsonify({
            'success': True,
            "response": "user update"}
        )
        return response, 200

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})


@main.route('/', methods=['DELETE'])
def destroy():
    try:
        id = request.json['id']

        if id is None:
            response = jsonify({
                'success': False,
                "response": "user id is required"}
            )
            return response, 401

        _user = User(id, None, None, None)
        UserService.destroy(_user)

        response = jsonify({
            'success': True,
            "response": "user destroyed"}
        )
        return response, 200

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})
