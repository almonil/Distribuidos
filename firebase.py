import firebase_admin
from firebase_admin import exceptions


from firebase_admin import credentials
from firebase_admin import db 

firebase_sdk = credentials.Certificate('C:/Users/USER/colliers_ai/distribuidos-56d73-firebase-adminsdk-pebax-60904ee74c.json')

firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://distribuidos-56d73-default-rtdb.firebaseio.com'})

datos = {
    "usuarios": {
        "name": "jose Sebastian",
        "descripcion" : "Es un estudiante"},
        "name": "Alfonso",
        "descripcion" : "Es un estudiante"
      
}


ref = db.reference("datos")

import json


