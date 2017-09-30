"""Config handler.

All config variables should be accessible just via this library.
"""
import os
from configparser import ConfigParser

# global variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, "config/stage.ini")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "templates/static/")


class Config:
    """Config handler class."""

    # do not manipulate this variable
    _cur_section = None

    def __init__(self):
        """Initialize Config class."""
        self._c = ConfigParser()
        try:
            self._c.read(CONFIG_FILE)
        except:
            pass # FIXME: need to handle exception

    def section(self, section_name: str) -> Config:
        """Select a config section.

        :param str section_name: section name
        :return: return Config object
        :rtype: Config
        """
        self._cur_section = section_name
        return self

    def get(self, key_name: str, cast=str) -> str:
        """Get value of a variable in mentioned section.

        :param str key_name: key name
        :param type cast: cast result
        :return: variable value
        :rtype: str
        """
        result = self._c[self._cur_section][key_name]
        try:
            return cast(result)
        except:
            pass # FIXME: handle exceptions
        return result
