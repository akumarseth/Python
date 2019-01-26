from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

@manager.command
def hello():
    print("hello")

if __name__ == '__main__':
    manager.run()


# python Flask_migrate_ex.py db init #creates migrate script and creates db
# python Flask_migrate_ex.py db migrate # creates migration script inside the migrate/version folder
# python Flask_migrate_ex.py db upgrade
# python Flask_migrate_ex.py db --help
# python Flask_migrate_ex.py db --shell# open shell

# python Flask_migrate_ex.py runserver # to run thevsript

# python Flask_migrate_ex.py hello # to invoke hello method

