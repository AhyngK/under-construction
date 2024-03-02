from mysql_manager import MySQLManager


def save_connection(artist, album):
    session = MySQLManager.Session()
