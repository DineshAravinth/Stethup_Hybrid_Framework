import configparser

config = configparser.RawConfigParser()
config.read("/Users/apple/Stethup_Project/STETHUP_PROJECT/Configurations/config.ini")

class Readconfig:
    @staticmethod   # We can directly call the method using class name
    def get_url():
        url=config.get('common info','url')
        return url

    @staticmethod
    def get_email():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
