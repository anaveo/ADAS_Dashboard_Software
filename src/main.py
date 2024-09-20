from PySide6.QtWidgets import QApplication
import sys
import os
import qasync
import asyncio
import json
from src.main_application import MainApplication
import logging.config

import logging
logger = logging.getLogger('main')


def setup_logging(config_path=None):
    if config_path is None:
        # Get the absolute path of the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the logging_config.json file
        config_path = os.path.join(script_dir, '../config/logging_config.json')

    with open(config_path, 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)


async def main():
    # Initialize main application
    main_app = MainApplication(config_path='../config/config.json')
    await main_app.init_mvc()
    main_app.run()
    logger.info("Application started.")

    # Keep the async event loop running for Qt events
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        logger.info("Interrupted by user.")
        await main_app.cleanup()


if __name__ == '__main__':
    # Set up logging
    setup_logging()

    # Create the QApplication before starting qasync event loop
    app = QApplication(sys.argv)

    # Set up qasync event loop
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)

    try:
        # Start the asyncio event loop integrated with the Qt event loop
        with loop:
            loop.run_until_complete(main())
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        logging.info("Application exited.")
