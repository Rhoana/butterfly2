from Settings import *
import numpy as np
import logging

class Query():
    content_types = [
        'application/{fmt}',
        'image/{fmt}'
    ]
    METADATA = INFOMETHODS[0]
    IMAGE_METH_LIST = DATAMETHODS
    GROUP_METH_LIST = GROUPMETHODS
    GROUP_LIST = GROUPTERMS
    TILE_LIST = TILETERMS
    DATA_LIST = DATATERMS
    INFO_LIST = INFOTERMS
    SPACE_LIST = POSITION
    FORM = TILETERMS[0]
    VIEW = TILETERMS[1]
    PATH = TILETERMS[2]
    DISK = TILETERMS[3]
    TYPE = DATATERMS[0]
    BLOCK = DATATERMS[1]
    NAME = INFOTERMS[0]
    METH = INFOTERMS[1]
    LIST = INFOTERMS[2]
    raw = {}

    def __init__(self,*args,**kwargs):
        pass

    def grouper(self, _method):
        return GROUPINGS.get(_method,'')

    def get_getter(self, _pos, _default):
        return lambda self: self.raw.get(_pos,_default)

    def make_getter(self, _list, _default):
        for pos in getattr(self, _list, []):
            getter = self.get_getter(pos, _default)
            setattr(Query, pos, property(getter))

    def att(self,k):
        return getattr(self,k)

    def getatt(self,k):
        return self.att(self.att(k))

    @property
    def is_data(self):
        return self.att(self.METH) in self.IMAGE_METH_LIST

    def log(self,action,**kwargs):
        statuses = {
            'miss': 'info'
        }
        actions ={
            'miss': 'Missing {lost} from {group}'
        }
        status = statuses[action]
        message = actions[action].format(**kwargs)
        getattr(logging, status)(message)
        return message