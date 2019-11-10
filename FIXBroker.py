from __future__ import (
    absolute_import, 
    division, 
    print_function,
    unicode_literals
)

import collections

from backtrader import BrokerBase, Order, BuyOrder, SellOrder
from backtrader.utils.py3 import with_metaclass
from backtrader.comminfo import CommInfoBase
from backtrader.position import Position

import FIXStore

class FIXCommInfo(CommInfoBase):
    def getvaluesize(self, size, price):
        pass

    def getoperationcost(self, size, price):
        pass


class MetaFIXBroker(BrokerBase.__class__):
    def __init__(cls, name, bases, dct):
        '''Class has already been created ... register'''
        # Initialize the class
        super(MetaFIXBroker, cls).__init__(name, bases, dct)
        FIXStore.BrokerCls = cls


class FIXBroker(with_metaclass(MetaFIXBroker, BrokerBase)):
    def __init__(self, **kwargs):
        pass

    def start(self):
        pass

    def data_started(self, data):
        pass

    def stop(self):
        pass

    def getcash(self):
        pass

    def getvalue(self):
        pass

    def getposition(self, data, clone=True):
        pass

    def orderstatus(self, order):
        pass

    def buy(self, owner, data,
            size, price=None, plimit=None,
            exectype=None, valid=None, tradeid=0, oco=None,
            trailamount=None, trailpercent=None,
            parent=None, transmit=True,
            **kwargs):
        pass

    def sell(self, owner, data,
             size, price=None, plimit=None,
             exectype=None, valid=None, tradeid=0, oco=None,
             trailamount=None, trailpercent=None,
             parent=None, transmit=True,
             **kwargs):
        pass

    def cancel(self, order):
        pass

    def notify(self, order):
        pass

    def get_notification(self):
        pass

    def next(self):
        pass

    