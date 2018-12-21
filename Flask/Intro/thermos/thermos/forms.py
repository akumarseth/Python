from flask_wtf import form
from wtforms.fields import StringField
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, url

class BookmarkForm():
    url = URLField('url', validators=[DataRequired, url()])
    description = StringField('description')