import tornado.web


class ProjectHandler(tornado.web.RequestHandler):
    def get(self, project_id=None):
        self.write("project handler! {}".format(project_id))

    def head(self):
        # return modified_datetime
        pass
