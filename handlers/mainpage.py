from google.appengine.ext import db
from helpers import *
from handlers.blog import BlogHandler

class MainPage(BlogHandler):
    
  def get(self):
      
      ## get all posts 
      blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC")
      
      ## if posts, render
      if blogs:
          self.render("index.html", blogs=blogs) 
