import logging


class Singleton(type):
    # Inherit from "type" in order to gain access to method __call__
    def __init__(cls, *args, **kwargs):
        cls.__instance = None  # Create a variable to store the object reference
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            # if the object has not already been created
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            # if object reference already exists; return it
            return cls.__instance


class KLogger(metaclass=Singleton):
    def __init__(self):
        # create logger
        logger = logging.getLogger('koden')
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        self.logger = logger

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def fatal(self, message):
        self.logger.critical(message)