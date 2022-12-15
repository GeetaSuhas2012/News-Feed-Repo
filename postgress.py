import configparser

# Method to read config file settings
config = configparser.ConfigParser()
config.read('config.ini')
database = config['Postgress']['database']
user = config['Postgress']['user']
password = config['Postgress']['password']
host = config['Postgress']['host']
port = config['Postgress']['port']

print("\nDisplaying details\n")

print("database: " + database)
print("user: " + user)
print("host: " + host)

# connection = psycopg2.connect(database="dbname", user="username", password="Dreamjob@2022", host="hostname", port=5432)
#
# cursor = connection.cursor()