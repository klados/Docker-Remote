from application import app
from flask import render_template, request, redirect, url_for, flash, session
from application.services.dockerServiceApi import DockerServiceApi
from application.forms.auth import LoginForm, RegisterForm
from application.services.authService import AuthService
from application.midleware.authMidleware import login_required
from . import db
import math


@app.route("/")
def index():
    return render_template("index.html", index=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        loginService = AuthService(db).loginService(request.form)
        if loginService['status'] == 'success':
            flash(f"Welcome {loginService['username']}", "success")
            session['username'] = loginService['username']
            session['role'] = loginService['role']
            return redirect(url_for('index'))
        flash("Error please check your credentials", "danger")
    return render_template("login.html", login=True, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        registerService = AuthService(db).registerService(request.form)
        if len(registerService) != 0:
            for error in registerService:
                form[error['field']].errors.append(error['msg'])
        else:
            flash('Successfully registered, Please login', 'success')
            return redirect('/')
    return render_template("register.html", register=True, form=form)


@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/images")
@login_required
def images():
    page = request.args.get('page', default=1, type=int)
    perPage = 10
    offset = (page - 1) * perPage
    docker = DockerServiceApi()
    listImage = docker.getAllInstalledImages()
    totalPages = math.ceil(len(listImage) / perPage) + 1
    return render_template("images.html", images=True, totalPages=totalPages,
                           listImage=listImage[offset: offset + perPage])


@app.route('/deleteImage', methods=['POST'])
@login_required
def deleteImage():
    print('delete image', request.form)
    return redirect(url_for('images'))


@app.route("/containers")
@login_required
def containers():
    docker = DockerServiceApi()
    listContainers = docker.getAllRunningContainers()
    print(listContainers)
    return render_template("containers.html", containers=True, listContainers=listContainers)
