# -*- coding: utf-8 -*-
"""
Test module for endpoints.
@author: Charlie Lewis
"""
from poseidon.helpers.endpoint import Endpoint
from poseidon.helpers.endpoint import endpoint_factory
from poseidon.helpers.endpoint import EndpointDecoder


def test_Endpoint():
    """
    Tests Endpoint
    """
    endpoint = endpoint_factory('foo')
    b = endpoint.encode()
    c = EndpointDecoder(b).get_endpoint()
    a = {'tenant': 'foo', 'mac': '00:00:00:00:00:00'}
    hashed_val = Endpoint.make_hash(a)
    assert hashed_val != ''
