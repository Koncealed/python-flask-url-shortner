from flask import Flask, render_template, url_for, request, session, redirect, flash
from pymongo import MongoClient
import random
import string
client = MongoClient('mongodb://robbie:password@ds119302.mlab.com:19302/bitcoin')
db = client.bitcoin.users

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    return build_link(request.form['link'])

@app.route('/<s>')
def link(s):
    link = get_url(s)
    return redirect('http://{}'.format(link) if 'http://' not in link or 'https://' not in link else link if is_exsisting(s) else url_for('index'))

#Functions vvvv

def build_link(url):
    new_link = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(4, 12)))
    if check_link(new_link, url):
        add_link(new_link,url)
        print('Passed Check, and adding to DB')
        return new_link
    build_link(url)
def add_link(short,url):
    db.insert({'short': short, 'url': url})

def check_link(short,link):
    return db.find({'short' : short, 'url' : link }).count() == 0 # Makes sure link hasn't been created yet

def is_exsisting(i): #
    return db.find({'short' : i}).count() >= 1

def get_url(s):
    return db.find_one({'short' : s})['url']

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run()