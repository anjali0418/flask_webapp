from flask import Flask, render_template, request
import csv

#app creation
app = Flask(__name__)

with open("exam_dates.csv") as file: #automatically closes file
  reader = csv.reader(file)
  header = next(reader)
  dates_list = [row for row in reader]
  print(dates_list)

#main page
@app.route('/')
def index():
    return render_template("index.html")

#after filling in subject required in first page
@app.route('/subject_required')
def subject():
  input = request.args.get("subject").lower()
  
  #submission validation
  if not input:
    return render_template("input_error.html", message="No input")

  for subject in dates_list:
    if input in subject: #subject exists in list
      return render_template("required_subject.html", date=subject[-1], text=subject[0].capitalize()+" Repository")
  #if input not found in list
  return render_template("input_error.html", message="You have input an invalid input.")

app.run(host='0.0.0.0', port=81)
