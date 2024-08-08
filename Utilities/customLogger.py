import logging
import os
import warnings


class LogGen:
    @staticmethod
    def loggen():
        log_directory = "/Users/apple/Automation/STETHUP_PROJECT/Logs"

        # Create the log directory if it doesn't exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
            print(f"Created directory: {log_directory}")

        log_filename = os.path.join(log_directory, "automation.log")
        print(f"Log file path: {log_filename}")

        # Clear previous logging configuration
        logging.shutdown()
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # Configure logging
        logging.basicConfig(
            filename=log_filename,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO
        )

        logger = logging.getLogger()

        # Check if logger has handlers
        if not logger.handlers:
            # Add console handler to see logs in the console
            logger.addHandler(logging.StreamHandler())

        print("Logger configured.")

        # Redirect warnings to the logger
        logging.captureWarnings(True)
        warnings.showwarning = lambda message, category, filename, lineno, file=None, line=None: logger.warning(
            f"{category.__name__}: {message} (from {filename}:{lineno})"
        )

        return logger
