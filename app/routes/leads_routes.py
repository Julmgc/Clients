
import flask
from app.models.leads_model import Leads
from flask import Blueprint, jsonify, request
from sqlalchemy import exc

bp_leads = Blueprint('vaccine', __name__, url_prefix='/api')

@bp_leads.route('/lead', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def get_create():
  if flask.request.method == 'POST':
    try:
      data = request.json
      if not Leads.check_keys(**data):
        return "You must send name, email and phone data and they must be string type"
      if Leads.check_phone_format(**data):
        return "Phone must be in this format: (xx)xxxxx-xxxx"
      return Leads.insert_user(**data) 
    except exc.IntegrityError:
      return 'Email and name already exist', 409

  if flask.request.method == 'GET':
    try:
      return jsonify(Leads.get_all_users())
    except exc.OperationalError: 
      return 'Database does not exist', 204

  if flask.request.method == 'PATCH':
    try:
      data = request.json
      if Leads.check_data_key(**data):
        if Leads.patch_user_data(**data) == None:
          return "User does not exist", 404
        return "", 200
      else:
        return "You can only send key email through the patch route" 
    except exc.IntegrityError:
      return "User does not exist", 404

  if flask.request.method == 'DELETE':
    try:
      data = request.json
      if Leads.check_data_key(**data):
        if Leads.delete_user_data(**data) == None:
          return "User does not exist", 404
        return "", 200
      else:
        return "You can only send key email through the patch route"
    except exc.IntegrityError:
      return "User does not exist", 404
    

