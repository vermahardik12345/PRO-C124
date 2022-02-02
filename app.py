from flask import Flask,jsonify,request

app = Flask(__name__)

contacts=[
    {
        'Contact':9911184801,
        'Name':'Maria',
        'done':False,
        'id':1
    },
    {
        'Contact':9911084800,
        'Name':'James',
        'done':False,
        'id':2
    }

]


@app.route("/")
def hello_world():
    return "Hello, Welcome to my api"

@app.route("/add-data",methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the details"
        },400)
    contact={
    'id':contacts[-1]['id']+1,
    'Contact':request.json['Contact'],
    'Name':request.json.get('Name',""),
    "done":False
    }

    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"Contact Added Successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":contacts
    })

if (__name__ == '__main__'):
    app.run(debug=True)
