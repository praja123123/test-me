from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__, static_url_path='/static')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db_csv:
        names = ['email', 'subject', 'body']
        writer = csv.DictWriter(db_csv, fieldnames=names)
        if not os.path.getsize('database.csv'):
            writer.writeheader()
        writer.writerow(data)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/<string:page_name>')
def href_page_name(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "error"