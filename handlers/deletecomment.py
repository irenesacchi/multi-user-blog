from google.appengine.ext import db
from models.comment import Comment
from handlers.blog import BlogHandler
from models.post import Blog
from helpers import *


class DeleteComment(BlogHandler):

    def get(self, post_id, comment_id):
        post = Blog.get_by_id(int(post_id), parent=blog_key())
        if not post:
            self.write("The post does not exist")
            return

        ## get comment
        comment = Comment.get_by_id(int(comment_id))

        ## if comments
        if comment:

            ## if author = comments
            if comment.user.name == self.user.name:

                ## delete comment
                db.delete(comment)
                time.sleep(0.1)
                self.redirect('/post/%s' % str(post_id))

            ## else error
            else:
                self.write("Ups. you can't do that!")

        ## else error
        else:
            self.write("The comment does not exist")
