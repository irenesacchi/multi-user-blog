from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment
from models.like import Like
from models.user import User
from helpers import *

class EditPost(BlogHandler):

    def get(self, post_id):
        if not self.user:
            self.redirect('/login')
        else:
            key = db.Key.from_path("Blog", int(post_id), parent=blog_key())
            post = db.get(key)
            user_id = User.by_name(self.user.name)
            comments_count = Comment.count_by_blog_id(post)
            post_comments = Comment.all_by_blog_id(post)
            likes = Like.by_blog_id(post.key().id())
            like_count = Like.by_blog_id(post.key().id())
            if not like_count:
                like_count=0

            ## user = author
            if post.user.key().id() == User.by_name(self.user.name).key().id():

                ## render edit post
                self.render("editpost.html", post=post)

            ## else error
            else:
                error = "Ups. you can't edit someone's else post!"
                self.render("post.html",
                            post=post,
                            likes=likes,
                            like_count=like_count,
                            post_comments=post_comments,
                            comments_count=comments_count,
                            error=error)
    def post(self, post_id):
        if not self.user:
            self.redirect("/login")
        else:
            key = db.Key.from_path("Blog", int(post_id), parent=blog_key())
            post = db.get(key)

            if post:

                ## request update
                if self.request.get("update"):

                    ## subject, content and user
                    subject = self.request.get("subject")
                    content = self.request.get("content").replace('\n', '<br>')

                    ## user = author
                    if post.user.key().id() == User.by_name(self.user.name).key().id():

                        ## subject and content
                        if subject and content:

                            ## update
                            post.subject = subject
                            post.content = content
                            post.put()
                            time.sleep(0.1)
                            self.redirect('/post/%s' % str(post.key().id()))

                        ## else error
                        else:
                            post_error = "Please enter a subject and the blog content"
                            self.render(
                            "editpost.html",
                            subject=subject,
                            content=content,
                            post_error=post_error)

                    ## else error
                    else:
                        error = "Ups. you can't edit someone's else post!"
                        self.render("post.html",
                                    post=post,
                                    likes=likes,
                                    post_comments=post_comments,
                                    comments_count=comments_count,
                                    like_count=like_count,
                                    error=error)

                ## if cancel
                elif self.request.get("cancel"):
                    self.redirect('/post/%s' % str(post.key().id()))

            else:
                self.write("The post does not exist")
