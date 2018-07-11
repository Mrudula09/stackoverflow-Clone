import _mysql
import sys
import MySQLdb as sqldb
import click
import os.path
import urllib.request
import django
from stackoverflowClone import settings

@click.group()
def sqlDB():
    "perform different sql operations using python"
    pass

def connect():
    "connects to mysql server"
    try:
        database = sqldb.connect('localhost', 'root', 'root')
        return  database
    except sqldb.Error as e:
        return None

def connectToDataBase(dbname):
    "connects to given database of MySQL server"
    try:
        connection = sqldb.connect('localhost', 'root', 'root', dbname)
        return connection
    except sqldb.Error :
        return None

@sqlDB.command("createdb",short_help="creates a database and tables")
def createdb():
    dbname=settings.DATABASES['default']['NAME']
    db = connect()
    if db is None:
        click.echo('Error occured while connecting to datase')
        sys.exit(1)
    click.echo('creating  a database..')
    sqlquery = db.cursor()
    sqlquery.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
    db.commit()
    pass


@sqlDB.command("dropdb",short_help="drops a database")
def dropdb():
    dbname = settings.DATABASES['default']['NAME']
    db=connectToDataBase(dbname)
    if db is None:
        click.echo('Error occured while connecting to datase')
        sys.exit(1)
    sqlquery=db.cursor()
    sqlquery.execute(f'DROP DATABASE IF EXISTS {dbname}')
    db.commit()
    click.echo(f"Database {dbname} is dropped")

if __name__=='__main__':
    sqlDB()