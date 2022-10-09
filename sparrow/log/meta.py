import logging

import six


class LoggingMixinMeta(type):
    @property
    def logger(cls):
        if '_log' in cls.__dict__:
            return cls._log
        cls._log = logging.root.getChild(
            cls.__module__ + '.' + cls.__name__
        )
        return cls._log
