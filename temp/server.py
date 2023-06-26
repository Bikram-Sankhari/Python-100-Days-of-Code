from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# with app.app_context():
#     db.create_all()

new_user = User(email="banti",
                password="pass",
                name="banti",
                )

# with app.app_context():
#     db.session.add(new_user)
#     db.session.commit()
#
#     print(new_user.id)
# with app.app_context():
#     result = db.session.execute(db.select(User).where(User.id == 1)).first()
#
#     print(type(result[0]))
