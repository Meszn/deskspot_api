from flask import Flask, jsonify
from app.config import Config
from app.extensions import db, jwt, ma, swagger


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Extensionları başlat
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    swagger.init_app(app)

    # Modelleri import et (DB oluşumu için gerekli)
    from app.models import user, desk, booking

    # Blueprintleri kaydet
    from app.routes.auth import auth_bp
    from app.routes.desk import desk_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(desk_bp, url_prefix='/api/desks')

    # Global Hata Yönetimi
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Kaynak bulunamadı"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Sunucu hatası"}), 500

    # Veritabanını oluştur (Development için pratik, production'da migration kullanılır)
    with app.app_context():
        db.create_all()

    return app