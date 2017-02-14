from google.appengine.ext import db
from models.post import Blog
from handlers.blog import BlogHandler
from models.comment import Comment
from models.user import User
from helpers import *

class EditComment(BlogHandler):

    def get(self, post_id, comment_id):

        ## get blog and comment
        post = Blog.get_by_id(int(post_id), parent=blog_key())
        comment = Comment.get_by_id(int(comment_id))
        key = db.Key.from_path("Blog", int(post_id), parent=blog_key())
        user_id = User.by_name(self.user.name)
        comments_count = Comment.count_by_blog_id(post)
        post_comments = Comment.all_by_blog_id(post)
        ## if comment:
        if comment:

            ## author=comment
            if comment.user.name == self.user.name:

                ## render edit comment page
                self.render("editcomment.html", comment_text=comment.text)

            ## else error
            else:
                error = "Ups. you can't do that!"
                self.render("editcomment.html", edit_error=error)

        ## else error
        else:
            error = "The comment does not exist"
            self.render("editcomment.html", edit_error=error)

    def post(self, post_id, comment_id):
        if self.user:
            ## if update:
            if self.request.get("update_comment"):
                ## get comment
                comment = Comment.get_by_id(int(comment_id))
                comment.text = self.request.get('comment_text')
                ## user=author
                if comment.user.name == self.user.name:
                    if comment.text:
                        comment.put()
                        time.sleep(0.1)
                        self.redirect('/post/%s' % str(post_id))
                    else:
                        error = "please fill in the content of your comment"
                        self.render("editcomment.html",
                                comment_text=comment.text,
                                edit_error=error,
                                comment=comment)
                ## else error
                else:
                    error = "Ups. you can't do that!"
                    self.render(
                        "editcomment.html",
                        comment_text=comment.text,
                        edit_error=error)

            ## if cancel redirect
            elif self.request.get("cancel"):
                self.redirect('/post/%s' % str(post_id))

        else:
            self.redirect("/login")
