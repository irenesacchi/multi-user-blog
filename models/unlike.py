from google.appengine.ext import db
from helpers import *
from models.post import Blog
from models.user import User

class Unlike(db.Model):
    post = db.ReferenceProperty(Blog, required=True)
    user = db.ReferenceProperty(User, required=True)

    # get number of unlikes for blog id
    @classmethod
    def by_blog_id(cls, blog_id):
        ul = Unlike.all().filter('post =', blog_id)
        return ul.count()

    # get number of unlikes for blog and user id
    @classmethod
    def check_unlike(cls, blog_id, user_id):
        cul = Unlike.all().filter(
            'post =', blog_id).filter(
            'user =', user_id)
        return cul.count()

 
