import logging
import os


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
        return logger


# Test the logger setup
# if __name__ == "__main__":
#     logger = LogGen.loggen()
#     logger.info("This is a test log message.")
