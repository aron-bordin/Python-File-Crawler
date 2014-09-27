#!/usr/bin/python3
from db import db
import settings as s

def run_tests():
    d = db(s.host, s.username, s.password, s.database)
    d.connect()
    print(d.select("select * from files"))


if __name__ == "__main__":
    run_tests()