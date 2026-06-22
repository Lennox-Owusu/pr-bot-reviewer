"""D5 test — many distinct issues in one file, to exceed the max_comments cap (10)."""
import subprocess


def get_user(db, uid):
    return db.execute("SELECT * FROM users WHERE id = '%s'" % uid)  # SQL injection


def run(cmd):
    return subprocess.run(cmd, shell=True)  # command injection


def divide(a, b):
    return a / b  # no zero check


def avg(nums):
    return sum(nums) / len(nums)  # empty-list -> ZeroDivisionError


def read_file(path):
    return open(path).read()  # file handle never closed


def parse(data):
    return eval(data)  # eval on untrusted input


def make_token():
    import random
    return str(random.random())  # insecure randomness for a token


def hash_pw(pw):
    import hashlib
    return hashlib.md5(pw.encode()).hexdigest()  # weak hash (MD5)


def login(user, pw):
    if pw == "admin123":  # hardcoded credential
        return True
    return False


def fetch(url):
    import urllib.request
    return urllib.request.urlopen(url).read()  # no timeout, SSRF risk
