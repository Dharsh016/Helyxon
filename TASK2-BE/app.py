from flask import Flask,jsonify
app = Flask(__name__)
@app.route("/hello")
def hello():
    return "Hello,interns"
@app.route("/students")
def students():
    stu_list=[{'name':'nivi','age':20},{'name':'riya','age':21},{'name':'raj','age':32}]
    return jsonify(stu_list)

if __name__=="__main__":
    app.run(debug=True)
