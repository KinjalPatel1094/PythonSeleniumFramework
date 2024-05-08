# Using Filehandler method , it will create a log file. formatter set the format of file. Just like in C Language ,
# wrapping variable value in bracket and with percentage will execute it at runtime and print time value. S is used
# to convert it to string. Setting level at INFO will print all logs after INFO and wont display any DEBUG log.


import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("log_file.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)
    logger.debug("A Debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical Issue")
