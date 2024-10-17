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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path to the logging_config.json file
    config_path = os.path.join(script_dir, '../config/config.json')
    can_config_path = os.path.join(script_dir, '../config/can_config.json')

    # Initialize main application
    main_app = MainApplication(config_path=config_path, can_config_path=can_config_path)
    await main_app.init_comms_managers()
    await main_app.init_mvc()
    try:
        main_app.run()
    except Exception as e:
        logger.error(f"Error running application: {e}")
        raise e

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
        with loop:
            loop.run_until_complete(main())
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        # Ensure cleanup is called regardless of how the program exits
        try:
            loop.run_until_complete(main_app.cleanup())  # Ensure proper async cleanup
        except Exception as cleanup_error:
            logger.error(f"Error during cleanup: {cleanup_error}")
        logging.info("Application exited.")
