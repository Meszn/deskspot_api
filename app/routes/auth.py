from flask import Blueprint, request, jsonify
from app.models.user import User
from app.extensions import db, jwt
from app.schemas.schemas import UserSchema
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Yeni kullanıcı kaydı
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
    responses:
      201:
        description: Kullanıcı oluşturuldu
      400:
        description: Kullanıcı zaten var
    """
    data = request.get_json()

    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return jsonify({"message": "Kullanıcı zaten mevcut"}), 400

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Kayıt başarılı"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Kullanıcı Girişi ve JWT Token alma
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Token döner
      401:
        description: Geçersiz kimlik
    """
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()

    if user and user.check_password(data.get('password')):
        # Token içine user identity ve admin bilgisini gömüyoruz
        additional_claims = {"is_admin": user.is_admin}
        access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200

    return jsonify({"message": "Geçersiz kullanıcı adı veya şifre"}), 401