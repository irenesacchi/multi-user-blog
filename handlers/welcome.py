from handlers.blog import BlogHandler

class Welcome(BlogHandler):
    
    def get(self):
        
        ## check user log-in
        if self.user:

            ## welcome + username
            self.render('welcome.html', username = self.user.name)

            ## else signup
        else:
            self.redirect('/signup')
