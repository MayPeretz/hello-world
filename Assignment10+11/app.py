from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from pages.assignment10.assignment10 import assignment10
import mysql.connector

app = Flask(__name__)
app.register_blueprint(assignment10)

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

def connector(query, query_type: str):
    return_value = False
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 database="web_database")
    cursor = db.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        db.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result
    db.close()
    cursor.close()
    return return_value

@app.route("/assignment11/users", methods=["GET"])
def users():
    if request.method == 'GET':
        result = connector("SELECT * FROM users", query_type="fetch")
        if len(result) == 0:
            return jsonify({
                'success': 'False: User not found',
                "data": []
            })
        else:
            return jsonify({
                'success': 'True: User found',
                "data": result
            })

@app.route('/assignment11/users/selected', defaults={'user_id': 7}, methods=['GET'])
@app.route('/assignment11/users/selected/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if request.method == 'GET':
        result = connector("SELECT * FROM users WHERE UserID='%s'" % user_id, query_type="fetch")
        if len(result) == 0:
            return jsonify({
                'success': 'False',
                "data": []
            })
        else:
            return jsonify({
                'success': 'True',
                "data": result
            })
if __name__ == '__main__':
    app.run()
