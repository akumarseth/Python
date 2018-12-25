from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
# from logging import DEBUG
from forms import BookmarkForm

app = Flask(__name__)
# app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = b'\x94\x02\xbf\x86\x16\x89\xbf\tt\xc6\xa7\xb0\x9c$\x94\x13\xb5\xef\xbb\xe0\x9afP\x89'

bookmarks = []

def store_bookmarks(url):
    bookmarks.append(dict(
        url = url,
        user = "Abhishek",
        date=datetime.utcnow()
    ))

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    # return render_template('index.html', title="Title pass from view to template",
    #                        text=["first", "second","third"])
    # return render_template('index.html', title="Title pass from view to template", user=User("Abhishek", "Kumar"))
    return  render_template('index.html', new_bookmarks = new_bookmarks(5), title="Title pass from view to template", user=User("Abhishek", "Kumar"))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    # if request.method == "POST":
    if form.validate_on_submit():
        url=request.form['url']
        store_bookmarks(url)
        # app.logger.debug("stored url: " + url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

