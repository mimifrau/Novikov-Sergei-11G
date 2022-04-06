import hashlib
from datetime import datetime
from init import db


class klient(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(20), unique=True)
    e_mail = db.Column(db.String(80), unique=True)
    nickname = db.Column(db.DateTime)
    birthday = db.Column(db.DateTime)
    date_of_reg = db.Column(db.String(256), unique=True, nullable=False)



class tovar(db.Model):
    id_tovar = db.Column(db.Integer, primary_key=True)
    kol_vo = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(10000), unique=True, nullable=False)
    price = db.Column(db.Float, unique=True, nullable=False)
    def __repr__(self):
        return f'[{self.id}] {self.name}'


class zakaz(db.Model):
    id_products = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    adress = db.Column(db.String(80))
    id_zakaz = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'[{self.id}] {self.name}'




db.create_all()



if __name__ == '__main__':
    pass

db.session.commit()

