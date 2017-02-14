from google.appengine.ext import db
from models.post import Blog
from handlers.blog import BlogHandler
from models.comment import Comment
from models.like import Like
from models.user import User
from helpers import *


class DeletePost(BlogHandler):

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

        if not post:
            self.write("The post does not exist")
            return

        ## if user = author
        if post.user.key().id() == User.by_name(self.user.name).key().id():

            ## delete post
            db.delete(key)
            time.sleep(0.1)
            self.render("deletepost.html",
                        post=post,
                        likes=likes,
                        like_count=like_count,
                        post_comments=post_comments,
                        comments_count=comments_count,)
        ## else error
        else:
            error = "You cannot delete other user's posts"
            self.render(
                "post.html",
                post=post,
                likes=likes,
                like_count=like_count,
                post_comments=post_comments,
                comments_count=comments_count,
                error=error)
