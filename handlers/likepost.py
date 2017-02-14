from google.appengine.ext import db
from models.post import Blog
from handlers.blog import BlogHandler
from models.user import User
from models.like import Like
from models.comment import Comment
from helpers import *


class LikePost(BlogHandler):

    def get(self, post_id):

            key = db.Key.from_path("Blog", int(post_id), parent=blog_key())
            post = db.get(key)
            if not post:
                self.write("The post does not exist")
                return
            user_id = User.by_name(self.user.name)
            likes = Like.by_blog_id(post.key().id())
            previously_liked = Like.check_like(post.key().id(), self.user.key())
            comments_count = Comment.count_by_blog_id(post)
            post_comments = Comment.all_by_blog_id(post)
            like_count = Like.by_blog_id(post.key().id())
            if not like_count:
                like_count=0

            if self.user:
                if post.user.key().id() != User.by_name(self.user.name).key().id():
                    if previously_liked == 0:
                        l = Like(
                            post=post, user=User.by_name(
                                self.user.name))
                        l.put()
                        time.sleep(0.1)
                        self.redirect('/post/%s' % str(post.key().id()))
                    else:
                        error = "You've already liked this post"
                        self.render(
                            "post.html",
                            post=post,
                            likes=likes,
                            like_count=like_count,
                            post_comments=post_comments,
                            comments_count=comments_count,
                            error=error)
                else:
                    error = "You cannot like your own posts"
                    self.render(
                        "post.html",
                        post=post,
                        likes=likes,
                        like_count=like_count,
                        post_comments=post_comments,
                        comments_count=comments_count,
                        error=error)

            else:
                self.redirect("/login")
