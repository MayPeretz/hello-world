from flask import Blueprint, render_template, request
import mysql.connector

assignment10 = Blueprint (
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment10',
    template_folder='templates'
)

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

@assignment10.route('/assignment10', methods=['GET', 'POST'])
def show():
    # connector("INSERT INTO users VALUES(7, 'Michael', 'Lawson','michael.lawson@reqres.in');", "commit")
    # connector("INSERT INTO users VALUES(8, 'Lindsay', 'Ferguson', 'lindsay.ferguson@reqres.in');", "commit")
    # connector("INSERT INTO users VALUES(9, 'Tobias', 'Funke', 'tobias.funke@reqres.in');", "commit")
    # connector("INSERT INTO users VALUES(10, 'Byron', 'Fields', 'byron.fields@reqres.in');", "commit")
    # connector("INSERT INTO users VALUES(11, 'George', 'Edwards', 'george.edwards@reqres.in');", "commit")
    # connector("INSERT INTO users VALUES(12, 'Rachel', 'Howell', 'rachel.howell@reqres.in');", "commit")
    if request.method == 'POST' and request.form.get('form_type') == 'show':
        all = connector("SELECT * FROM USERS", "fetch")
        return render_template('assignment10.html', method='POST', type='show', data=all)
    if request.method == 'POST' and request.form['form_type'] == 'insert':
        first = request.form['first_name']
        last = request.form['last_name']
        email = request.form['email']
        insert = "INSERT INTO users (First_Name, Last_Name, Email) VALUES ('%s', '%s', '%s')" % (first, last, email)
        connector(insert, "commit")
        all = connector("SELECT * FROM USERS", "fetch")
        return render_template('assignment10.html', method='POST', type='insert', data=all)
    if request.method == 'POST' and request.form['form_type'] == 'update':
        userid = request.form['user_id']
        checkID = connector("SELECT * FROM USERS WHERE UserID = '%s' " % userid, "fetch")
        if len(checkID) == 0:
            return render_template('assignment10.html', method='POST', type='update', found=False)
        else:
            first = request.form['first_name']
            last = request.form['last_name']
            email = request.form['email']
            update = "UPDATE users SET First_Name='%s', Last_Name='%s', Email='%s' WHERE UserID='%s'" % (first, last, email, userid)
            connector(update, "commit")
            all = connector("SELECT * FROM USERS", "fetch")
            return render_template('assignment10.html', method='POST', type='update', found=True, data=all)
    if request.method == 'POST' and request.form['form_type'] == 'delete':
        userid = request.form['user_id']
        checkID = connector("SELECT * FROM USERS WHERE UserID = '%s' " % userid, "fetch")
        if len(checkID) == 0:
            return render_template('assignment10.html', method='POST', type='delete', found=False)
        else:
            delete = "DELETE FROM users WHERE UserID='%s'" % (userid)
            connector(delete, "commit")
            all = connector("SELECT * FROM USERS", "fetch")
            return render_template('assignment10.html', method='POST', type='delete', found=True, data=all)
    return render_template('assignment10.html')