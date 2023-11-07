from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from __main__ import app
from schema import Reading, db
import datetime



@app.route('/')
def index():
    return render_template('show-readings.html', readings=Reading.query.all())



@app.route('/add-new-reading-form', methods = ['GET', 'POST'])
def add_new_reading_form():
    return render_template('add-new-reading-form.html', readings=Reading.query.all())


@app.route('/add-new-reading', methods = ['GET', 'POST'])
def add_new_reading():
    form_data = request.form.to_dict(flat=False)
    new_reading = Reading(form_data)
    db.session.add(new_reading)
    db.session.commit()
    return redirect("/")

@app.route('/delete-reading', methods = ['GET', 'POST'])
def delete_reading():
    args = request.args
    Reading.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/")
