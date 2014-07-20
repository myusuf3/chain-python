#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

DEFAULT_CHAIN_URL = 'https://api.chain.com/{version}/{blockchain}'


class Chain(object):

    def __init__(self, api_key, blockchain='bitcoin', version='v1'):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.auth = (api_key, '')
        self.blockchain = blockchain
        self.api_version = version
        self.base_url = DEFAULT_CHAIN_URL.format(version=self.api_version,
            blockchain=self.blockchain,
        )

    def _get(self, path, data={}):
        path = self.base_url + path
        data.update({'key': self.api_key})
        response = self.session.get(path, params=data)
        print response.request.url
        return response

    def _put(self, path, payload, data={}):
        path = self.base_url + path
        response = self.session.put(path, data=payload, params=data)
        print response.request.url
        return response


    def get_address(self, address):
        path = "/addresses/{address}".format(
            address=address
        )
        response = self._get(path)
        return response.json()

    def get_addresses(self, addresses):
        if len(addresses) <= 200:
            return self.get_address(','.join(addresses))
        else:
            raise ValueError('You provided more than the allowed 200 addresses')


    def get_address_transaction(self, address, limit=50):
        data = {'limit': limit}
        path = "/addresses/{address}/transactions".format(
            address=address,
            )
        response = self._get(path, data=data)
        return response.json()

    def get_address_transactions(self, addresses, limit=50):
        if len(addresses) <= 200:
            return self.get_address_transaction(','.join(addresses), limit=limit)
        else:
            raise ValueError('You provided more than the allowed 200 addresses')

    def get_address_unspents(self, address):
        path = "/addresses/{address}/unspents".format(address=address)
        response = self._get(path)
        return response.json()

    def get_addresses_unspents(self, addresses):
        if len(addresses) <= 200:
            return self.get_address_unspents(','.join(addresses))
        else:
            raise ValueError('You provided more than the allowed 200 addresses')

    def get_address_op_returns(self, address):
        path =  '/addresses/{address}/op-returns'.format(address=address)
        response = self._get(path)
        return response.json()

    def get_transaction(self, thash):
        path = '/transactions/{hash}'.format(hash=thash)
        repsonse = self._get(path)
        return repsonse.json()

    def get_transaction_op_return(self, thash):
        path = '/transactions/{hash}/op-return'.format(hash=thash)
        response = self._get(path)
        return response.json()

    def send_transaction(self, thex):
        path = '/transactions'
        payload = {'hex':thex}
        response = self._put(path, payload)
        return response.json()

    def get_block(self, hash_or_height):
        path = '/blocks/{hash}'.format(hash=hash_or_height)
        response = self._get(path)
        return response.json()

    def get_latest_block(self):
        path = '/blocks/latest'
        response = self._get(path)
        return response.json()






















