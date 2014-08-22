__author__ = 'TeaEra'


class Singleton(object):
    """
    Design pattern:
      Singleton
    """

    _instances = {}

    def __new__(cls, *args, **kwargs):
        if not cls in cls._instances:
            cls._instances[cls] = \
                super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class SingletonClass(Singleton):
    """
    """

    pass