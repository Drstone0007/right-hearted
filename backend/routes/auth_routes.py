from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, UserMixin
# For simplicity, we'll use a hardcoded admin; in production, use models
auth_bp = Blueprint('auth', __name__)

class DummyUser(UserMixin):
    def __init__(self, id): self.id = id

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'admin':
            user = DummyUser(1)
            login_user(user)
            return redirect(url_for('dashboard.index'))
        flash('Invalid credentials')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
