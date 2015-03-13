# -*- coding: utf-8 -*-
__author__ = 'alarin'

from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient() #клиент
medical = client.medical #база

patients = medical.patients #коллекция


def addPatient(patient):
    patients.insert(patient.__dict__)


def getAllPatients():
    """
    :return: все пациенты
    """
    return patients.find()


def clearAll():
    patients.delete_many()


def patientGone(id):
    patients.update({'_id': ObjectId(id)},
                     {'$set': {"state":"gone"}})

def getPatient(id):
    return patients.find_one({"_id":ObjectId(id)})

def removePatient(id):
    patients.remove({"_id":ObjectId(id)})