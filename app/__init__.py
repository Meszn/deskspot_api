from flask import Flask, jsonify
from app.config import Config
from app.extensions import db, jwt, ma, swagger


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 1. Extensionları (Eklentileri) Başlat
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    # --- SWAGGER AYARLARI (Authorize Butonu İçin - DÜZELTİLMİŞ) ---
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "DeskSpot API",
            "description": "Ortak Çalışma Alanı Rezervasyon Sistemi API Dokümantasyonu",
            "contact": {
                "responsibleOrganization": "DeskSpot Inc.",
                "responsibleDeveloper": "Geliştirici",
                "email": "iletisim@deskspot.com",
                "url": "www.deskspot.com",
            },
            "termsOfService": "www.deskspot.com/terms",
            "version": "1.0.0"
        },
        # "host": "localhost:5000",  <-- BU SATIRI SİLDİK (Otomatik algılasın)
        # "schemes": ["http", "https"], <-- BU SATIRI SİLDİK (Otomatik algılasın)
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Token başına 'Bearer ' ekleyerek giriniz. Örn: 'Bearer eyJhbGc...'"
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }

    swagger.template = swagger_template
    swagger.init_app(app)
    # --------------------------------

    # 2. Modelleri import et
    from app.models import user, desk, booking

    # 3. Blueprintleri (Rotaları) Kaydet
    from app.routes.auth import auth_bp
    from app.routes.desk import desk_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(desk_bp, url_prefix='/api/desks')

    # 4. Global Hata Yönetimi
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Kaynak bulunamadı"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Sunucu hatası"}), 500

    # 5. Veritabanını oluştur
    with app.app_context():
        db.create_all()

    return app
