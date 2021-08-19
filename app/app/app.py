from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_migrate import Migrate
from flask_user import current_user, login_required, UserManager, user_manager
import json, datetime, os
from dotenv import load_dotenv

load_dotenv()

from database import db, User, Role, app

with open('static/js/app/manifest.json') as json_file:
    js_assets = json.load(json_file)

js_assets = {key: 'js/app/' + js_assets[key].replace('auto', '') for key in js_assets.keys()}

contact_email = os.getenv('contact_email', 'contact_email_not_set_in_config')

user_manager = UserManager(app, db, User)

def initiate():

    if not User.query.first():
        user = User(
            email='admin@flask.app',
            username='admin',
            email_confirmed_at=datetime.datetime.utcnow(),
            password=user_manager.hash_password('secret'),
            first_name='admin',
            last_name='admin'
        )
        user.roles.append(Role(name='Admin'))
        db.session.add(user)
        db.session.commit()

try:
    initiate()
except Exception as e:
    print('Init error', e)
    pass

migrate = Migrate(app, db)

def create_app():


    from blueprints.home import get_home_blueprint
    app.register_blueprint(get_home_blueprint())

    from blueprints.users import get_users_blueprint
    app.register_blueprint(get_users_blueprint(user_manager))

    @app.route('/protected/<string:filename>')
    @login_required
    def protected(filename):
        return send_from_directory(
            'protected/',
            filename
        )

    @app.route('/protected/custom_dir/<string:filename>')
    @login_required
    def protected_import(filename):
        return send_from_directory(
            'protected/custom_dir/',
            filename
        )

    @app.context_processor
    def inject_model():
        current_user_email = None
        try:
            current_user_email = current_user.email
        except Exception as e:
            pass
        return dict(jsAssets=js_assets, currentUserEmail=current_user_email)

    return app