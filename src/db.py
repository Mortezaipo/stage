"""Database library.

All activity on database should be handle by this library.
# FIXME : make it singletone
# FIXME : validate psycopg integrity errors
"""
import psycopg2 as pgsql
import psycopg2.extras as pgsql_extras

from settings import Settings


class DB:
    """Database handler class."""

    def __init__(self):
        """Initialize DB class."""
        self._settings = Settings().section("DATABASE")
        self._con = pgsql.connect(dbname=self._settings.get("dbname"),
                                  host=self._settings.get("host"),
                                  port=self._settings.get("port"),
                                  user=self._settings.get("username"),
                                  password=self._settings.get("password"))
        self._cur = self._con.cursor(cursor_factory=pgsql_extras.DictCursor)

    def select(self, query: str, data: tuple=()) -> list:
        """Execute select query to fetch all records.

        :param str query: query string
        :param tuple data: data which should be append inside of query
        :return: fetched records
        :rtype: list
        """
        self._cur.execute(query, data)
        data = self._cur.fetchall()
        return data

    def select_one(self, query: str, data: tuple=()) -> dict:
        """Execute select query to fetch one record.

        :param str query: query string
        :param tuple data: data which should be append inside of query
        :return: fetched record
        :rtype: dict
        """
        self._cur.execute(query, data)
        data = self._cur.fetchone()
        return data

    def insert(self, query: str, data: tuple) -> bool:
        """Insert data in database.

        :param str query: query string
        :param tuple data: data which should be append inside of query
        :return: action status
        :rtype: bool
        """
        self._cur.execute(query, data)
        try:
            self._con.commit()
            return True
        except pgsql.DatabaseError:
            self._con.rollback()
        return False

    def update(self, query: str, data: tuple) -> bool:
        """Update data in database.

        :param str query: query string
        :param tuple data: data which should be append inside of query
        :return: action status
        :rtype: bool
        """
        self._cur.execute(query, data)
        try:
            self._con.commit()
            return True
        except pgsql.DatabaseError:
            self._con.rollback()
        return False

    def delete(self, query: str, data: tuple=()) -> bool:
        """Delete records in database.

        :param str query: query string
        :param tuple data: data which should be append inside of query
        :return: action status
        :rtype: bool
        """
        self._cur.execute(query, data)
        try:
            self._con.commit()
            return True
        except pgsql.DatabaseError:
            self._con.rollback()
        return False

db = DB()