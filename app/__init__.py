from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .models import models
    with app.app_context():
        db.create_all()
        if not models.Negara.query.first():
            db.session.add(models.Negara(negara="Indonesia",totalBencanaAlam = 1))
            db.session.commit()
        if not models.BencanaAlam.query.first():
            db.session.add(models.BencanaAlam(id_negara = 1,tipe="gempa bumi",nama="Gempa Sumatra Barat",tahun=2009))
            db.session.commit()

    # from app.controllers.product_controller import product_bp
    # from app.controllers.category_controller import category_bp
    from app.controllers import controller_bp
    app.register_blueprint(controller_bp)
    
    return app
