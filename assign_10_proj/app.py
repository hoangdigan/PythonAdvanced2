import os
import data.db_session as db_session
from data.customer import Customer
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_

app = Flask(__name__)

def setup_db():
    db_file = os.path.join(os.path.dirname(__file__), 'db', 'Northwind_small.sqlite')
    db_session.global_init(db_file)

@app.route('/')
def home():
    all_data=session.query(Customer)
    return render_template("home.html", customers=all_data)

@app.route('/searchname')
def searchName():
    all_data = session.query(Customer)
    return render_template("searchName.html", customers=all_data)

@app.route('/searchid')
def searchID():
    all_data = session.query(Customer)
    return render_template("searchID.html", customers=all_data)

@app.route('/searchnameid')
def searchNameID():
    all_data = session.query(Customer)
    return render_template("searchNameID.html", customers=all_data)

# SEARCH NAME
@app.route('/searchlike', methods=['GET', 'POST'])
def searchlike():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = "%{}%".format(tag)
            customers = session.query(Customer).filter(Customer.company_name.like(search))
            return render_template('searchName.html', customers=customers)

    return render_template('searchName.html', customers=customers)

@app.route('/searchnotlike', methods=['GET', 'POST'])
def searchnotlike():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = "%{}%".format(tag)
            customers = session.query(Customer).filter(Customer.company_name.not_like(search))
            return render_template('searchName.html', customers=customers)

    return render_template('searchName.html', customers=customers)

@app.route('/searchcontains', methods=['GET', 'POST'])
def searchcontains():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag

            customers = session.query(Customer).filter(Customer.company_name.contains(search))
            return render_template('searchName.html', customers=customers)

    return render_template('searchName.html', customers=customers)

@app.route('/searchstartwith', methods=['GET', 'POST'])
def searchstartwith():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag

            customers = session.query(Customer).filter(Customer.company_name.startswith(search))
            return render_template('searchName.html', customers=customers)

    return render_template('searchName.html', customers=customers)

@app.route('/searchendwith', methods=['GET', 'POST'])
def searchendwith():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag

            customers = session.query(Customer).filter(Customer.company_name.endswith(search))
            return render_template('searchName.html', customers=customers)

    return render_template('searchName.html', customers=customers)

# SEARCH ID
@app.route('/searchequals', methods=['GET', 'POST'])
def searchEquals():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag
            customers = session.query(Customer).filter(Customer.id == search)
            return render_template('searchID.html', customers=customers)

    return render_template('searchID.html', customers=customers)

@app.route('/searchnotequals', methods=['GET', 'POST'])
def searchNotEquals():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag
            customers = session.query(Customer).filter(Customer.id != search)
            return render_template('searchID.html', customers=customers)

    return render_template('searchID.html', customers=customers)

@app.route('/searchgreaterthan', methods=['GET', 'POST'])
def searchGreaterThan():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag
            customers = session.query(Customer).filter(Customer.id > search)
            return render_template('searchID.html', customers=customers)

    return render_template('searchID.html', customers=customers)

@app.route('/searchlessthan', methods=['GET', 'POST'])
def searchLessThan():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag
            customers = session.query(Customer).filter(Customer.id < search)
            return render_template('searchID.html', customers=customers)

    return render_template('searchID.html', customers=customers)

@app.route('/searchin', methods=['GET', 'POST'])
def searchIn():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag.split(",")
            customers = session.query(Customer).filter(Customer.id.in_(search))
            return render_template('searchID.html', customers=customers)

    return render_template('searchID.html', customers=customers)

@app.route('/searchinnegated', methods=['GET', 'POST'])
def searchInNegated():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag.split(",")
            customers = session.query(Customer).filter(~Customer.id.in_(search))
            return render_template('searchID.html', customers=customers)

    return render_template('searchID.html', customers=customers)

@app.route('/searchnotin', methods=['GET', 'POST'])
def searchNotIn():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            tag = request.form["tag"]
            search = tag.split(",")
            customers = session.query(Customer).filter(Customer.id.not_in(search))
            return render_template('searchID.html', customers=customers)

    return render_template('searchID.html', customers=customers)

# SEARCH ID & NAME
@app.route('/searchand', methods=['GET', 'POST'])
def searchAnd():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['tag']:
            flash('Please enter all the fields', 'error')
        else:
            name = request.form["name"]
            id = request.form["id"]

            customers = session.query(Customer).filter(and_(Customer.id == id, Customer.company_name == name))
            return render_template('searchNameID.html', customers=customers)

    return render_template('searchNameID.html', customers=customers)


@app.route('/searchor', methods=['GET', 'POST'])
def searchOr():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            name = request.form["name"]
            id = request.form["id"]

            customers = session.query(Customer).filter(or_(Customer.id == id, Customer.company_name == name))
            return render_template('searchNameID.html', customers=customers)

    return render_template('searchNameID.html', customers=customers)

@app.route('/searchmultifilter', methods=['GET', 'POST'])
def searchMultiFilter():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            name = request.form["name"]
            id = request.form["id"]

            customers = session.query(Customer).filter(Customer.id == id).filter(Customer.company_name == name)
            return render_template('searchNameID.html', customers=customers)

    return render_template('searchNameID.html', customers=customers)

@app.route('/searchmultifilterone', methods=['GET', 'POST'])
def searchMultiFilterOne():
    customers = session.query(Customer)
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            name = request.form["name"]
            id = request.form["id"]

            customers = session.query(Customer).filter(Customer.id == id, Customer.company_name == name)
            return render_template('searchNameID.html', customers=customers)

    return render_template('searchNameID.html', customers=customers)


if __name__ == '__main__':
    setup_db()
    session = db_session.factory()
    app.run(debug=True)
    session.close()
