"""Stage main application file."""
import tornado.web
import tornado.httpserver
import tornado.ioloop

import settings
from settings import Settings
import page
import post
import project
import contact
import auth

app = tornado.web.Application(
    handlers = [
        (r"/$", page.PageHandler),
        (r"/pages/(?P<page_id>\w*)", page.PageHandler),
        (r"/posts/(?P<post_id>\w*)", post.PostHandler),
        (r"/projects/(?P<project_id>\d*)", project.ProjectHandler),
        (r"/contact/", contact.ContactHandler),
        (r"/auth/$", auth.AuthHandler),
        (r"/auth/register/$", auth.RegisterHandler)
    ],
    template_path = settings.TEMPLATE_DIR,
    static_path = settings.STATIC_DIR,
    ui_modules = {"page_menus": page.PageUIModule},
    cookie_secret = Settings().section("SECURITY").get("cookie_secret")
)

http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(int(Settings().section("GENERAL").get("port")))
tornado.ioloop.IOLoop.instance().start()
