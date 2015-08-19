# bin/env python
# coding: utf-8

__author__ = 'Moch'

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")