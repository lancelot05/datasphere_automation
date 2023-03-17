from flask import Flask, render_template, request
import uploadJson

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def automation():
   if request.method == "POST":
       url = request.form.get("url")
       email = request.form.get("email")
       password = request.form.get("password")
       space = request.form.get("space")
       json_file_path = request.form.get("jsondir")
       uploadJson.process(url,email,password,space,json_file_path)
       return "Processing"
   return render_template('index.html')

if __name__ == '__main__':
   app