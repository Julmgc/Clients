
import flask
import sqlalchemy
from app.models.leads_model import Leads
from flask import Blueprint, jsonify, request
from sqlalchemy import exc

bp_leads = Blueprint('vaccine', __name__, url_prefix='/api')

@bp_leads.route('/clients', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def get_create():
    if flask.request.method == 'POST':
        try:
            data = request.json
            if not Leads.check_keys(**data):
                return jsonify({"message": "You must send name, email and phone data and they must be string type"}) , 406
            if Leads.check_phone_format(**data):
                return jsonify({"message": "Phone must be in this format: (xx)xxxxx-xxxx"}), 406
            return Leads.insert_user(**data), 201
        except exc.IntegrityError:
            return jsonify({"message": "Email, name or phone already exist"}), 409
        except TypeError:
            return jsonify({"message": "You must send name, email and phone data and they must be string type"}), 406


    if flask.request.method == 'GET':
        try:
            return jsonify(Leads.get_all_users())
        except exc.OperationalError: 
            return jsonify({"message": "Database does not exist"}), 204

    if flask.request.method == 'PATCH':
        try:
            data = request.json
            if Leads.check_data_key(**data):
                if Leads.patch_user_data(**data) == None:
                    return jsonify({"message": "User does not exist"}), 404          
                return Leads.patch_user_data(**data), 200
            else:
                return jsonify({"message": "You can only send key email through the patch route"}), 406 
        except exc.IntegrityError:
            return jsonify({"message": "User does not exist"}), 404 
        except AttributeError:
            return jsonify({"message": "User does not exist"}), 404

    if flask.request.method == 'DELETE':
        try:
            data = request.json
            if Leads.check_data_key(**data):
                if not Leads.delete_user_data(**data):
                    return jsonify({"message": "User does not exist"}), 404   
                return jsonify(""), 204
            else:
                return jsonify({"message": "You can only send key email through the patch route"}), 406
        except exc.IntegrityError:
            return jsonify({"message": "User does not exist"}), 404 

      

