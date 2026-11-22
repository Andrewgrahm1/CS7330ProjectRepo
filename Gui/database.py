
import mysql.connector
import configparser
from pathlib import Path


def connect_db():

    # Find and read the configuration file
    config = configparser.ConfigParser()

    config_path = Path(__file__).parent / "config.ini"
    config.read(config_path)

    # Connect to MySQL
    connection = mysql.connector.connect(
        host=config["mysql"]["host"],
        port=config.getint("mysql", "port"),
        user=config["mysql"]["user"],
        password=config["mysql"]["password"],
        database=config["mysql"]["database"]
    )

    return connection
