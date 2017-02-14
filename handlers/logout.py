from handlers.blog import BlogHandler

class Logout(BlogHandler):
    def get(self):

        ## check if logged in
        if self.user:

            ## logout
            self.logout()
            self.redirect('/signup')

        ## else error
        else:
            msg = "please log-in first"
            self.render('login.html', error = msg)
