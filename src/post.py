import tornado.web


class PostHandler(tornado.web.RequestHandler):
    def get(self, post_id=None):
        self.write("post handler! {}".format(post_id))

    def head(self):
        # return modified_datetime
        pass
