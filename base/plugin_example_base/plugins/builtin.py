__author__ = 'bunjiboys'

import logging

log = logging.getLogger(__name__)

class BuiltInPlugin(object):
    def run(self, *args, **kwargs):
        log.info('run method executed. self: {self}, args: {args}, kwargs: {kwargs}'.format(
            self=str(self),
            args=", ".join(args),
            kwargs=", ".join( [ "{0}={1}".format(k, v) for k,v in kwargs.items() ] )
        ))

    @staticmethod
    def run_static(*args, **kwargs):
        log.info('run_static method executed. args: {args}, kwargs: {kwargs}'.format(
            args=", ".join(args),
            kwargs=", ".join( [ "{0}={1}".format(k, v) for k,v in kwargs.items() ] )
        ))
