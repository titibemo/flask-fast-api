import os
import logging
import structlog


LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE = os.path.join(LOG_DIR, "logs.log")


def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)

    # ---- Handlers ----
    file_handler = logging.FileHandler(LOG_FILE)
    console_handler = logging.StreamHandler()

    # ---- Formatter structlog (IMPORTANT) ----
    formatter = structlog.stdlib.ProcessorFormatter(
        processor=structlog.processors.JSONRenderer(),  # fichier = JSON propre
    )

    file_handler.setFormatter(formatter)

    console_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
            processor=structlog.dev.ConsoleRenderer(colors=True),
        )
    )

    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, console_handler],
    )

    # ---- structlog config ----
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            structlog.processors.CallsiteParameterAdder(
                {
                    structlog.processors.CallsiteParameter.MODULE,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                    structlog.processors.CallsiteParameter.LINENO,
                }
            ),
            structlog.processors.add_log_level,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )