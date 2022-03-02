import email
import csv
#from inspect import _SourceObjectType
from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def my_home():
     return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
     return render_template(page_name)

    
def write_to_file(data):
     with open('database.txt', mode="a") as database:
          email = data["email"]
          subject = data["subject"]
          message = data["message"]
          file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
     with open('database.csv', newline="", mode="a") as database2:
          email = data["email"]
          subject = data["subject"]
          message = data["message"]
          csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
     if request.method=="POST":
          data = request.form.to_dict()
          write_to_csv(data)
          print(data)
          return redirect('/thankyou.html')
     else:
          return "something went wrong"

# @app.route('/components.html')
# def components():
#      return render_template("components.html")

# @app.route('/contact.html')
# def contact():
#       return render_template("contact.html")

# @app.route('/works.html')
# def works():
#      return render_template("works.html")

# <!DOCTOR html>
# <html>
# <head>
#     <title>MY WEBSITE</title>
#     <link rel="stylesheet"type="text/css" href="static/style.css">
#     <link rel="shortcut icon" href="{{ url_for('static', filename='tree.ico') }}">
# </head>
# <body>
#     {{ name }}
#     {{ post_id }}
#     <script src="static/script.js"></script>
# </body>
# </html> 