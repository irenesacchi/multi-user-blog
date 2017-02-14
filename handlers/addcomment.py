from google.appengine.ext import db
from models.post import Blog
from handlers.blog import BlogHandler
from models.user import User
from models.like import Like
from models.comment import Comment
from helpers import *


class AddComment(BlogHandler):

    def post(self, post_id):
        key = db.Key.from_path("Blog", int(post_id), parent=blog_key())
        post = db.get(key)
        user_id = User.by_name(self.user.name)
        comments_count = Comment.count_by_blog_id(key)
        post_comments = Comment.all_by_blog_id(key)
        likes = Like.by_blog_id(post.key().id())
        like_count = Like.by_blog_id(post.key().id())
        if not like_count:
            like_count=0

        if self.user:
            comment_text = self.request.get("comment_text")
            if comment_text:
                c = Comment(
                    post=key, user=self.user.key(), text=comment_text)
                c.put()
                time.sleep(0.1)
                self.redirect('/post/%s' % str(post.key().id()))
            else:
                comment_error = "Please enter a comment in the text area to post"
                self.render(
                    "post.html",
                    post=post,
                    comments_count=comments_count,
                    post_comments=post_comments,
                    likes=likes,
                    like_count=like_count,
                    comment_error=comment_error)
        else:
            self.redirect("/login")
