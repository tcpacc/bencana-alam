from .. import db

class Negara(db.Model):
    __tablename__ ="negara"
    id = db.Column(db.Integer, primary_key=True)
    negara = db.Column(db.String(100), nullable=False)
    totalBencanaAlam = db.Column(db.Integer, nullable = False)
    bencanaAlam = db.relationship('BencanaAlam', backref='Negara', lazy=True)

    @staticmethod
    def get_all():
        return Negara.query.all()

    # @staticmethod
    # def get_by_id(id):
    #     return Category.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def add_total(self):
        self.totalBencanaAlam+=1
        db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()


class BencanaAlam(db.Model):
    __tablename__= "bencanaalam"
    id = db.Column(db.Integer, primary_key=True)
    id_negara = db.Column(db.Integer,db.ForeignKey('negara.id'),nullable =False)
    tipe = db.Column(db.String(100), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    tahun = db.Column(db.Integer, nullable=False)

    @staticmethod
    def get_all():
        return BencanaAlam.query.all()

    # @staticmethod
    # def get_by_id(id):
    #     return Product.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
