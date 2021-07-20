import configparser

config = configparser.ConfigParser()
config.read('../setting.ini')

# MYSQL
HOST = config['mysql']['host']
PORT = config['mysql']['port']
DBNAME = config['mysql']['dbname']
UNAME = config['mysql']['uname']
UPASS = config['mysql']['upass']
