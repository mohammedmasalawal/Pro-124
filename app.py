// importing Flask 
from flask import Flask,jsonify,request
// to initialize app 
app=Flask(__name__)

# create an array of task
data=[
    {
        'id': 1,
         'contact ': u'9892071134',
         'name': u'jack',
         'done': False
         
    },
{
    'id':2,
    'contact': u'8369192263',
    'name':u'jane',
    'done': False
}

]
@app.route("/add-data",methods=["POST"])
def adddata():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "provide the data"
        })
    task1={ 
        'id': data[-1]['id']+1,
         ' name ': request.json['name'],
         'contact': request.json.get('contact'," "),
         'done': False
         

    }
    data.append(data1)
    return jsonify({
            "status": "Sucsses",
            "message": " data added"
    })

    @app.route("/")
def helloWorld():
    return " hello world "

// run the programme
if (__name__=="__main__"):
    app.run(debug=True)


