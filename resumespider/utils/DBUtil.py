#!/usr/bin/python
# -*- coding:utf-8 -*-
# ====================================================================
# Project: 'resumespider'
# File: 'DBUtil.py'
# Description:
#    数据库相关工具类
# Author: Paul Zhou(paulzhousz@gmail.com)
# Created Time: '2016-06-24 14:54'
# Update Log:
#  1.
#  2.
# =====================================================================

import pymongo

from resumespider.items import ResumeItem
from resumespider.settings import MONGO_DATABASE, MONGO_URI


class DBUtil(object):
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DATABASE]
        self.proxies = self.db[ResumeItem.__name__]

    def closedb(self):
        self.client.close()
