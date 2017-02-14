from handlers.blog import BlogHandler
from models.user import User
from helpers import *


class Signup(BlogHandler):

    def get(self):
        self.render("signup-form.html")

    def post(self):
        have_error = False
        ## username, password, verify and emails
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        params = dict(username=self.username,
                      email=self.email)
        ## username not valid: error
        if not valid_username(self.username):
            params['error_username'] = "Not a valid username."
            have_error = True

        ## Email not valid: error
        if not valid_email(self.email):
            params['error_email'] = "Email not a valid."
            have_error = True

        ## Passw not valid: error
        if not valid_password(self.password):
            params['error_password'] = "Password not valid."
            have_error = True
        ## if password different from verify: error
        elif self.password != self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True
        ## keep params
        if have_error:
            self.render("signup-form.html", **params)

        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError

#______________________________________________________________________________
### Register___________________________________________________________________

class Register(Signup):
    def done(self):

        ## make sure the user doesn't already exist
        u = User.by_name(self.username)

        ## if username exists: error
        if u:
            msg = 'That user already exists.'
            self.render('signup-form.html', error_username = msg)

        ## else add
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/welcome')
