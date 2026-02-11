from flask import Blueprint, request, jsonify
from app.models.desk import Desk
from app.extensions import db
from app.schemas.schemas import DeskSchema
from flask_jwt_extended import jwt_required, get_jwt

desk_bp = Blueprint('desks', __name__)


@desk_bp.route('/', methods=['GET'])
def get_desks():
    """
    Tüm masaları listele
    ---
    tags:
      - Desks
    responses:
      200:
        description: Masa listesi
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    desks = Desk.query.paginate(page=page, per_page=per_page, error_out=False)
    result = DeskSchema(many=True).dump(desks.items)

    return jsonify({
        "data": result,
        "total": desks.total,
        "pages": desks.pages,
        "current_page": desks.page
    }), 200


@desk_bp.route('/', methods=['POST'])
@jwt_required()
def create_desk():
    """
    Yeni masa ekle (Sadece Admin)
    ---
    tags:
      - Desks
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            location:
              type: string
    responses:
      201:
        description: Masa oluşturuldu
      403:
        description: Yetkisiz işlem
    """
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"message": "Admin yetkisi gerekiyor"}), 403

    data = request.get_json()
    new_desk = Desk(name=data['name'], location=data.get('location', ''))

    db.session.add(new_desk)
    db.session.commit()

    return DeskSchema().jsonify(new_desk), 201