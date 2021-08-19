from flask import jsonify, Blueprint, render_template, request
from flask_user import login_required, roles_required, current_user

from database import db, app, User, Role, UserRoles

import random, string, datetime

def get_users_blueprint(user_manager):
    users = Blueprint('users', __name__)

    @users.route('/users')
    @roles_required('Admin')
    def route_users():
        return render_template('users.html')

    def get_users():
        db_users = User.query.all()
        return [{'email':user.email, 'roles': [role.name for role in user.roles]} for user in db_users]

    @users.route('/get-users')
    @roles_required('Admin')
    def route_get_users():
        return jsonify(get_users())

    @users.route('/get-roles')
    @roles_required('Admin')
    def route_get_roles():
        roles = Role.query.all()
        roles = [role.name for role in roles]
        return jsonify(roles)

    @users.route('/add-role', methods=["POST"])
    @roles_required('Admin')
    def route_add_role():
        user_email = request.form.get('user')
        role = request.form.get('role')
        user = User.query.filter(User.email == user_email).first()
        role = Role.query.filter(Role.name == role).first()
        user.roles.append(role)
        db.session.commit()
        return jsonify(True)

    @users.route('/remove-role', methods=["POST"])
    @roles_required('Admin')
    def route_remove_role():
        user_email = request.form.get('user')

        if current_user.email == user_email:
            return jsonify(False)

        role = request.form.get('role')
        user = User.query.filter(User.email == user_email).first()
        role = Role.query.filter(Role.name == role).first()
        UserRoles.query.filter(UserRoles.user_id == user.id).filter(UserRoles.role_id == role.id).delete()
        db.session.commit()
        return jsonify(True)

    @users.route('/delete-user', methods=["POST"])
    @roles_required('Admin')
    def route_delete_user():
        user_email = request.form.get('user')

        if current_user.email == user_email:
            return jsonify(False)

        User.query.filter(User.email == user_email).delete()
        db.session.commit()
        return jsonify(True)

    @users.route('/add-user', methods=["POST"])
    @roles_required('Admin')
    def route_add_user():
        email = request.form.get('email')
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        user = User(
            email=email,
            username=username,
            email_confirmed_at=datetime.datetime.utcnow(),
            password=user_manager.hash_password(password_string),
            first_name=first_name,
            last_name=last_name
        )

        db.session.add(user)
        db.session.commit()

        return jsonify(get_users())

    return users