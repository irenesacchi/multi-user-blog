from google.appengine.ext import db
from helpers import *
from user import User

class Blog(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    user = db.ReferenceProperty(User,
                                required = True,
                                collection_name="blogs")

    def render(self, current_user_id):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)
