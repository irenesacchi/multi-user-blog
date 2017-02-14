from handlers.blog import BlogHandler
from models.post import Blog
from models.user import User
from helpers import *

class NewPost(BlogHandler):
    
    def get(self):
        ## check if the user is logged in (self.user)
        if self.user:
            self.render("newpost.html")
        ## redirect login
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            return self.redirect('/')
        
        ## useranme, subject and content
        user_id = User.by_name(self.user.name)
        subject = self.request.get('subject')
        content = self.request.get('content').replace('\n', '<br>')

        ## if subject and content given: post page
        if subject and content:
            a = Blog(
                parent = blog_key(),
                user = user_id,
                subject = subject,
                content = content)
            a.put()
            self.redirect('/post/%s' % str(a.key().id()))

        ## otherwise error           
        else:
            error = "subject and content, please!"
            self.render(
                "newpost.html",
                subject=subject,
                content=content,
                error=error)
