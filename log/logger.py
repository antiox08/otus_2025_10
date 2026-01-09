import logging


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.FileHandler("test.log", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
