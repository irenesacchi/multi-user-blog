from handlers.blog import BlogHandler
from models.user import User

class Login(BlogHandler):
    
    def get(self):
        self.render('login-form.html')

    def post(self):

        ## get username and passw
        username = self.request.get('username')
        password = self.request.get('password')

        ## get user account
        u = User.login(username, password)

        ## if user account
        if u:

            ## login and redirect
            self.login(u)
            self.redirect('/welcome')

        ## else error           
        else:
            msg = 'Invalid login'
            self.render('login-form.html', error = msg)
