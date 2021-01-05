from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)


@app.route('/')
def HomePage():
    return render_template("May_Peretz_Mulla-CV.html")

@app.route('/contact')
def contactPage():
    return render_template("ContactForm.html")

@app.route('/UsersList')
def UsersListPage():
    return render_template("UsersList.html")

@app.route('/Assignment8')
def Assignment8():
    return render_template('assignment8.html',
                           FavoriteBooks={'The girl you left behind': 2012,
                                          'Me before you': 2012,
                                          'The giver of stars': 2019,
                                          'Again again': 2019,
                                          'The silent patient ':2020})

app.secret_key = 'MayPeretz250594'
@app.route('/assignment9', methods=['GET','POST'])
def assignment9():
    if request.method == 'GET':
        if 'method' and 'Search' in request.args:
            method=request.args ['method']
            Search=request.args ['Search']
            return render_template('assignment9.html', Tmethode=request.method, method=method, Search=Search)
        return render_template("assignment9.html")
    if request.method == 'POST':
        if 'username' and 'usermail' in request.form:
            session['username'] = request.form['username']
            session['email'] = request.form['usermail']
            session['loggedin'] = True
            return render_template('assignment9.html')
        return render_template("assignment9.html")

@app.route("/logout")
def logout():
    session['loggedin'] = False
    return redirect(url_for('assignment9'))

if __name__ == '__main__':
    app.run(debug=True)
