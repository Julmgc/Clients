import flask
from app.models.leads_model import Leads
from flask import Blueprint, jsonify, request, current_app
from sqlalchemy import exc

bp_leads = Blueprint('vaccine', __name__, url_prefix='/api')

# E-mail e telefone único;
# Telefone obrigatoriamente no formato (xx)xxxxx-xxxx.

@bp_leads.route('/lead', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def get_create():
  if flask.request.method == 'POST':
    try:
      data = request.json
      
      # Corpo da requisição obrigatoriamente
      #  apenas com name, email e phone, sendo todos os campos do tipo string.

      if Leads.is_phone_Valid(data['phone']):
        return "Cpf must contain 11 numbers"
      lead = Leads(**data)
      session = current_app.db.session
      session.add(lead)
      session.commit()
      data = lead.query_to_json()
      return data
    except exc.IntegrityError:
      return 'Cpf already exists', 400

  elif flask.request.method == 'GET':
    try:
      data = Vaccine.query.all()
      data_to_json = [ vaccine.query_to_json() for vaccine in data]
      return jsonify(data_to_json)
    except exc.OperationalError: 
      return 'Database does not exist', 204
  elif flask.request.method == 'PATCH':
    ...
  else:
    ...
