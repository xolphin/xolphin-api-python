#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests, json
from requests.auth import HTTPBasicAuth

from xolphin.endpoint.certificate import Certificate
from xolphin.endpoint.request import Request
from xolphin.endpoint.support import Support

try:
    from urllib.parse import urlencode # python 3
except ImportError:
    from urllib import urlencode


class Client(object):
    BASE_URL = 'https://api.xolphin.com/v1/'
    VERSION = '1.1'

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self._session = requests.session()
        self._session.headers.update({'Accept': 'application/json', 'User-Agent': 'xolphin-api-python/%s' % Client.VERSION})
        self._session.auth = HTTPBasicAuth(username, password)
        #self._session.proxies.update({
        #    'http': '127.0.0.1:8888',
        #    'https': '127.0.0.1:8888',
        #})
        #self._session.verify = False

    def get(self, method, data={}):
        response = self._session.get("%s%s" % (Client.BASE_URL, method), params=data)
        if 200 <= response.status_code < 300:
            return json.loads(response.content.decode('utf-8'))
        else:
            raise Exception(response.content)

    def download(self, method, data={}):
        response = self._session.get("%s%s" % (Client.BASE_URL, method), params=data)
        if 200 <= response.status_code < 300:
            return response
        else:
            raise Exception(response.content)

    def post(self, method, data={}):
        payload = {}
        for k in data:
            if k == 'document':
                payload[k] = ('document.pdf', str(data[k]), 'application/pdf')
            else:
                payload[k] = (None, str(data[k]))
        response = self._session.post("%s%s" % (Client.BASE_URL, method), files=payload)
        if 200 <= response.status_code < 300:
            return json.loads(response.content.decode('utf-8'))
        else:
            raise Exception(response.content)

    def request(self):
        return Request(self)

    def certificate(self):
        return Certificate(self)

    def support(self):
        return Support(self)

