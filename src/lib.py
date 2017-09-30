"""Extra functions.

This library prepars encryption and hashing functions.
"""
import hashlib
import time
from random import randint, sample


def generate_extra_data() > str:
    """Generate random extra data.

    :return: random extra data
    :rtype: str
    """
    part1 = randint(0, randint(1, 1000000000))
    part2 = sample(range(0, randint(30, 1000000000)), randint(0, randint(1, 30)))
    part3 = int(time.time()) + randint(0, randint(1, 1000000000))
    data = "{}{}{}".format(part1, "".join(map(str, part2)), part3)


def generate_password(password: str) -> str:
    """Generate password for memcached.

    :param str password: user password string
    :return: sha256 hash string
    :rtype: str
    """
    return hashlib.sha256(password.encode()).hexdigest()


def generate_hash(data: str) -> str:
    """Generate hash string.
    
    :param str data: sha256 data argument
    :return: hashed string
    :rtype: str
    """
    return hashlib.sha256(data.encode()).hexdigest()


def generate_token() -> str:
    """Generate user auth token.

    :return: token string
    :rtype: str
    """
    rand_data = generate_hash(generate_extra_data())
    return hashlib.sha256(rand_data).hexdigest()
