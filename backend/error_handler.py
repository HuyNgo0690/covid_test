import logging

from flask_restx import abort

from config.config import Config

logger = logging.getLogger(Config.LOGGER)


class HandleExceptions:
    @staticmethod
    def exception_to_http_response(error):
        (error_message,) = error.args
        logger.warning(f"<{error_message}>")
        abort(400, error_message)
