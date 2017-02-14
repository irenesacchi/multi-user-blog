# General
from webapp2 import WSGIApplication
from google.appengine.ext import db
from helpers import *

# Models
from models.post import Blog
from models.user import User
from models.comment import Comment
from models.like import Like
from models.unlike import Unlike

# Handlers
from handlers.mainpage import MainPage
from handlers.blog import BlogHandler
from handlers.signup import Signup, Register
from handlers.login import Login
from handlers.logout import Logout
from handlers.post import PostPage
from handlers.newpost import NewPost
from handlers.editpost import EditPost
from handlers.likepost import LikePost
from handlers.unlikepost import UnlikePost
from handlers.deletepost import DeletePost
from handlers.addcomment import AddComment
from handlers.deletecomment import DeleteComment
from handlers.editcomment import EditComment
from handlers.welcome import Welcome

#______________________________________________________________________________

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/welcome', Welcome),
                               ('/blog/?', MainPage),
                               ('/post/([0-9]+)', PostPage),
                               ('/newpost', NewPost),
                               ('/editpost/([0-9]+)', EditPost),
                               ('/post/([0-9]+)/like', LikePost),
                               ('/post/([0-9]+)/unlike', UnlikePost),
                               ('/deletepost/([0-9]+)', DeletePost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/([0-9]+)/addcomment', AddComment),
                               ('/blog/([0-9]+)/editcomment/([0-9]+)', EditComment),
                               ('/blog/([0-9]+)/deletecomment/([0-9]+)', DeleteComment),
                               ],
                              debug=True)
