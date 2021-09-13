from flask import Flask,request,jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app=Flask(__name__)
CORS(app)
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
conn=firestore.client()

@app.route("/task",methods=['POST','GET'])
def task_creation():
    status={}
    conn_obj=conn
    if request.method=='POST':
        data=request.get_json()
        print(data)
        try:
            conn_obj.collection('task').add(data)
            status['info']='inserted'
        except Exception as err:
            status['info']='not inserted'
            status['error']=str(err)
    
    elif request.method=='GET':
        print("hello")
        returndata={}
        try:
            data=conn.collection('task').get()
            for doc in data:
                doc_dict=doc.to_dict()
                doc_dict['id']=doc.id
                returndata[doc.id]=doc_dict
            status=returndata
        except Exception as err:
            status['info']='data error'
            status['error']=str(err)
    print(status)

    return status


@app.route("/task/<string:id>",methods=['DELETE','PUT'])
def task_updations(id):
    status={}
    if request.method=='PUT':
        try:
            data=request.get_json()
            conn.collection('task').document(id).update(data)
            status['info']='updated'
        except Exception as err:
            status['info']='not updated'
            status['error']=str(err)
    elif request.method=='DELETE':
        try:
            conn.collection('task').document(id).delete()
            status['info']='Deleted'
        except Exception as err:
            status['info']='not deleted'
            status['error']=str(err)
    return status   
app.run(host ='0.0.0.0', port = 5000, debug = True)
