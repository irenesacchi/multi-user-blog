from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.user import User
from models.comment import Comment
from models.like import Like
from helpers import *

class PostPage(BlogHandler):

    def get(self, blog_id):

        key = db.Key.from_path("Blog", int(blog_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        post_comments = Comment.all_by_blog_id(key)
        comments_count = Comment.count_by_blog_id(key)
        like_count = Like.by_blog_id(post.key().id())
        if not like_count:
            like_count=0
        self.render("post.html",
                    post=post,
                    comments_count = comments_count,
                    post_comments=post_comments,
                    like_count=like_count
                    )
