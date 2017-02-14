from google.appengine.ext import db
from helpers import *
from models.post import Blog
from models.user import User

class Like(db.Model):
    post = db.ReferenceProperty(Blog, required=True)
    user = db.ReferenceProperty(User, required=True)

    ## Numbers of likes for blog-id
    @classmethod
    def by_blog_id(cls, blog_id):
        key = db.Key.from_path("Blog", int(blog_id), parent=blog_key())
        post = db.get(key)
        l = Like.all().filter('post =', key)
        return l.count()

    # get number of likes for blog and user id
    @classmethod
    def check_like(cls, blog_id, user_key):
        key = db.Key.from_path("Blog", int(blog_id), parent=blog_key())
        post = db.get(key)
        cl = Like.all().filter(
            'post =', key).filter(
            'user =', user_key)
        return cl.count()
