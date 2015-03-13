# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import session, abort, jsonify, render_template, render_template_string, redirect, url_for
from Patient import Patient
import medicaldao

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", patients = medicaldao.getAllPatients())


@app.route('/add_patient', methods=["POST"])
def add_patient():
    if request.method == "POST":
        p = Patient(request.form["name"], request.form["age"])
        medicaldao.addPatient(p)
    return redirect("/")

@app.route('/patient/<id>', methods=["GET"])
def patient(id):
    return render_template("patient.html", p = medicaldao.getPatient(id))

@app.route('/patient/<id>/gone')
def patient_gone(id):
    medicaldao.patientGone(id)
    return redirect("/patient/%s" % id)

@app.route('/patient/<id>/delete')
def patient_delete(id):
    medicaldao.removePatient(id)
    return redirect("/")


if __name__ == '__main__':
    app.debug = True
    app.run()
