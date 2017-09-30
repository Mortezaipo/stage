"""Memcached library."""
import pylibmc

import lib
from settings import Settings


class Memcached:
    """Memcached class."""

    def __init__(self):
        """Initialize Memcached class."""
        self._settings = Settings().section("MEMCACHED")
        self._mc = pylibmc.Client(self._settings.get("host"), binary=True)
        self._mc.behaviors={"tcp_nodelay": True}

    def destroy_user_records(self, key_name: str):
        """Remove user memcached records.

        :param str key_name: memcached key name
        :rtype: void
        """
        self._mc.delete("user-".format(key_name))
        self._mc.delete("perm-".format(key_name))
        self._mc.delete("agent-".format(key_name))

    def get_user_id(self, key_name: str) -> str:
        """Get user id.

        :param str key_name: memcached key name
        :return: user id
        :rtype: str
        """
        return self._mc.get("user-".format(key_name))

    def get_user_permission(self, key_name: str) -> list:
        """Get user permission.

        :param str key_name: memcached key name
        :return: user permission
        :rtype: list
        """
        return self._mc.get("perm-{}".format(key_name))

    def get_user_agent(self, key_name):
        """Get user agent.

        :param str key_name: memcached key name
        :return: user logged in agent in hash code. it also contains ip address.
        :rtype: str
        """
        return self._mc.get("agent-{}".format(key_name))

    def set_user_id(self, user_id: int) -> bool:
        """Set user id.

        :param int user_id: user id
        :return: set action status
        :rtype: bool
        """
        action = self._mc.set("user-{}".format(lib.generate_token()), user_id)
        return action
