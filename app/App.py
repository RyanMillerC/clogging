import clogging 
from autologging import logged, traced

@logged
@traced
class App():
    """Example application class using clogging with autologging.
    """

    def __init__(self, message):
        self.__log.name = self.__class__.__name__ # Class name only
        self.message = message 
        self.__log.info("App instance created with message, %s"
                %(self.message))
