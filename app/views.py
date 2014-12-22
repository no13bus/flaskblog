from flask import render_template, flash, redirect
from app import app, lm
# from app import app, db, login_manager, oid, babel
from forms import LoginForm

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])


    
    # form = LoginForm()
    # if form.validate_on_submit():
    #     flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
    #     return redirect('/index')
    # return render_template('login.html',
    #     title = 'Sign In',
    #     form = form,
    #     providers = app.config['OPENID_PROVIDERS'])