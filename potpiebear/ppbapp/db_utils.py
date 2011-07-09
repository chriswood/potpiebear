#!/usr/bin/env python
# encoding: utf-8
"""
db_wrapper.py

Created by Chris Wood on 2011-06-25.

"""

import sys
import os
import unittest
import sqlite3

class db_wrapper:
    def __init__(self, db_path):
        self.conn_obj = sqlite3.connect(db_path)
        self.cursor = self.conn_obj.cursor()
        
    def get_users(self):
        sql = 'select * from users'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
    def get_songs(self):
        sql = 'select * from songs'
        self.cursor.execute(sql)
        return self.cursor.fetchall()


class db_wrapperTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()