import tornado.web


class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("contact handler!")

    def post(self):
        # return modified_datetime
        pass
