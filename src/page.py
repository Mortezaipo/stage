import tornado.web
from db import db
from settings import Settings


class PageHandler(tornado.web.RequestHandler):
    def get(self, page_id=None):
        cookie = self.get_secure_cookie(Settings().section("SECURITY").get("cookie_name"))
        if page_id:
            page_row = db.select("SELECT * FROM pages WHERE page_id=%s", (page_id,), True)
            edit_access = True
            self.render("pages/view.html", page_row=page_row, edit_access=edit_access)
        else:
            self.render("pages/home.html")

    def put(self, page_id):
        title = self.get_argument("title")
        body = self.get_argument("body")
        db.update("UPDATE pages SET title=%s, body=%s WHERE page_id=%s", (title, body, page_id))
        self.write("Updated!")

    def post(self, page_id=None):
        title = self.get_argument("title")
        body = self.get_argument("body")
        db.insert("INSERT INTO pages (title, body) values (%s, %s)", (title, body))
        self.write("Inserted!")

    def delete(self, page_id):
        db.delete("DELETE FROM pages WHERE page_id=%s", (page_id,))
        self.write("Deleted!")


class PageUIModule(tornado.web.UIModule):
    def render(self):
        page_rows = db.select("SELECT title from pages WHERE show_menu=false")
        result = ""
        for page in page_rows:
            result += "<li class=\"navbar-item\">"
            result += "<a class=\"nav-link\" href=\"#\">{}</a>".format(page["title"])
            result += "</li>"
        return result
