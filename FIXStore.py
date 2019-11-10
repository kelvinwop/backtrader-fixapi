from __future__ import (
    absolute_import, 
    division, 
    print_function,
    unicode_literals
)

import collections
from datetime import datetime, timedelta
import time as _time
import threading
import asyncio

import requests
import pandas as pd

import backtrader as bt
from backtrader.metabase import MetaParams
from backtrader.utils.py3 import queue, with_metaclass

class MetaSingleton(MetaParams):
    '''Metaclass to make a metaclassed class a singleton'''
    def __init__(cls, name, bases, dct):
        super(MetaSingleton, cls).__init__(name, bases, dct)
        cls._singleton = None

    def __call__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = (
                super(MetaSingleton, cls).__call__(*args, **kwargs))

        return cls._singleton


class FIXStore(with_metaclass(MetaSingleton, object)):
    @classmethod
    def getdata(cls, *args, **kwargs):
        pass

    @classmethod
    def getbroker(cls, *args, **kwargs):
        pass

    def __init__(self):
        pass

    def start(self, data=None, broker=None):
        pass
    
    def stop(self):
        pass

    def put_notification(self, msg, *args, **kwargs):
        pass

    def get_positions(self):
        pass

    def get_granularity(self, timeframe, compression):
        pass

    def get_instrument(self, dataname):
        pass

    def streaming_events(self, tmout=None):
        pass

    def _t_streaming_listener(self, q, tmout=None):
        pass

    def _t_streaming_events(self, q, tmout=None):
        pass

    def candles(self, dataname, dtbegin, dtend, timeframe, compression,
                candleFormat, includeFirst):
        pass

    def _t_candles(self, dataname, dtbegin, dtend, timeframe, compression,
                   candleFormat, includeFirst, q):
        pass

    def streaming_prices(self, dataname, tmout=None):
        pass

    def _t_streaming_prices(self, dataname, q, tmout):
        pass

    def get_cash(self):
        pass

    def get_value(self):
        pass

    def broker_threads(self):
        pass

    def _t_account(self):
        pass

    def order_create(self, order, stopside=None, takeside=None, **kwargs):
        pass

    def _t_order_create(self):
        pass

    def order_cancel(self, order):
        pass

    def _t_order_cancel(self):
        pass

    def _transaction(self, trans):
        pass

    def _process_transaction(self, old, trans):
        pass