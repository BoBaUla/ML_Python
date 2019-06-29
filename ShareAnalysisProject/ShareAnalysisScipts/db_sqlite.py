import sqlite3
from sqlite3 import Error
import os

table_datensatz_name = 'Datensatz'
fields_datensatz = [
    'id integer PRIMARY KEY autoincrement,', 
    'config_id integer,',
    'Werte blob null,',    
    'FOREIGN KEY (config_id) REFERENCES Konfiguration (id)']

table_configuration_name = 'Konfiguration'
fields_configuration = [
    'id integer PRIMARY KEY,', 
    'Datenpunkte integer,',
    'Guthaben integer,',
    'Transaktionsgebuehr integer,',
    'Schrittlaenge integer,', 
    'Strategienlimit integer,',
    'Kursstart integer,',
    'mu_rendite decimal,',
    'sigma_rendite decimal,',
    'StoppLoss decimal,',
    'SellAt decimal']

table_evaluation_name = 'Auswertungsmethode'
fields_evaluation = [
    'id integer PRIMARY KEY autoincrement,', 
    'name blob null'
]

table_results_name = 'Ergebniss'
field_results = [
    'id integer PRIMARY KEY autoincrement,', 
    'Scoure decimal,'
    'Kaeufe blob null,'
    'Verkaeufe blob null'
]

table_cross_name = 'Messung'
field_cross = [
    'id integer PRIMARY KEY autoincrement,', 
    'config_id integer,',
    'result_id integer,',
    'method_id integer,',
    'FOREIGN KEY (config_id) REFERENCES Konfiguration (id),'
    'FOREIGN KEY (result_id) REFERENCES Ergebniss (id),'
    'FOREIGN KEY (method_id) REFERENCES Auswertungsmethode (id)'
]


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_table_command(table_name, fields):
    cmd = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ( ' + ''.join( ' {} '.format(i) for i in fields) + ' );'
    return cmd

def init_db():
    cwd = os.getcwd()
    dbname = 'data.db'
    conn = create_connection(os.path.join(cwd, dbname))
    create_table(conn, create_table_command(table_configuration_name, fields_configuration))
    create_table(conn, create_table_command(table_datensatz_name, fields_datensatz))
    create_table(conn, create_table_command(table_evaluation_name, fields_evaluation))
    create_table(conn, create_table_command(table_results_name, field_results))
    create_table(conn, create_table_command(table_cross_name, field_cross))
