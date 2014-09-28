#!/usr/bin/python2
# coding:utf-8

from db import db
import settings as s
from crawler import Crawler


def run_tests():
    d = db(s.host, s.username, s.password, s.database)
    d.connect()


if __name__ == "__main__":
    run_tests()
    c = Crawler()
    c.run()