#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

DEFAULT_CHAIN_URL = 'https://api.chain.com/'


class Chain(object):

    def __init__(self, api_key, blockchain='bitcoin', version='v1'):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.auth = (api_key, '')
        self.blockchain = blockchain
        self.api_version = version

    def _get_response(self, path, data={}):
        data = data.update({'key': self.api_key})
        response = self.session.get(path, params=data)
        return response

    def get_address(self, address):
        path = "/{version}/{blockchain}/addresses/{address}".format(
            version=self.api_version,
            blockchain=self.blockchain,
            address=address
        )
        path = DEFAULT_CHAIN_URL + path
        response = self._get_response(path)
        return response.json()

    def get_addresses(self, addresses):
        return self.get_address(','.join(addresses))
