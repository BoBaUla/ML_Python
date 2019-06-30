import sqlite3
from sqlite3 import Error
import os

table_datensatz_name = 'Datensatz'
fields_datensatz = [
    'id integer PRIMARY KEY autoincrement,', 
    'config_id integer,',
    'Werte text,',    
    'FOREIGN KEY (config_id) REFERENCES Konfiguration (id)']

table_configuration_name = 'Konfiguration'
fields_configuration = [
    'id integer PRIMARY KEY autoincrement,'
    'config_id text,', 
    'Datenpunkte integer,',
    'Guthaben integer,',
    'Transaktionsgebuehr integer,',
    'Schrittlaenge integer,', 
    'Strategienlimit integer,',
    'Kursstart integer,',
    'mu_rendite double,',
    'sigma_rendite double,',
    'StoppLoss double,',
    'SellAt double']

table_evaluation_name = 'Auswertungsmethode'
fields_evaluation = [
    'id integer PRIMARY KEY autoincrement,', 
    'name text'
]

table_results_name = 'Ergebniss'
field_results = [
    'id integer PRIMARY KEY autoincrement,', 
    'Score decimal,'
    'Kaeufe text,'
    'Verkaeufe text'
]

table_cross_name = 'Messung'
field_cross = [
    'id integer PRIMARY KEY autoincrement,', 
    'data_id integer,',
    'result_id integer,',
    'method_id integer,',
    'FOREIGN KEY (data_id) REFERENCES ' +table_datensatz_name+' (id),'
    'FOREIGN KEY (result_id) REFERENCES ' +table_results_name+' (id),'
    'FOREIGN KEY (method_id) REFERENCES ' + table_evaluation_name+' (id)'
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

def location():
    cwd = os.getcwd()
    dbname = 'data.db'
    return os.path.join(cwd, dbname)

def init_db():
    conn = create_connection(location())
    create_table(conn, create_table_command(table_configuration_name, fields_configuration))
    create_table(conn, create_table_command(table_datensatz_name, fields_datensatz))
    create_table(conn, create_table_command(table_evaluation_name, fields_evaluation))
    create_table(conn, create_table_command(table_results_name, field_results))
    create_table(conn, create_table_command(table_cross_name, field_cross))

def insert_config(config):
    config_id = config.ConfigID()
    request = 'Select * from ' + table_configuration_name +' where config_id = ?;'
    conn = create_connection(location())
    id = 0
    with conn:
        cur = conn.cursor()
        cur.execute(request, (config_id,))
        rows = cur.fetchall()
        if len(rows) == 0:
            statement = 'insert into  ' + table_configuration_name +'''(
                config_id, 
                Datenpunkte, 
                Guthaben, 
                Transaktionsgebuehr, 
                Schrittlaenge, 
                Strategienlimit,
                Kursstart,
                mu_rendite,
                sigma_rendite,
                StoppLoss,
                SellAt) 
            values (?,?,?,?,?,?,?,?,?,?,?);
            '''
            values = config.GetValues()
            cur.execute(statement, values)
            id = cur.lastrowid
        else:
            id = rows[0][0]
    return id

def insert_result(result):
    conn = create_connection(location())
    id = 0
    with conn:
        cur = conn.cursor()
        cur.execute('insert into ' + table_results_name +'(Score, Kaeufe, Verkaeufe) values (?,?,?);', result)
        id = cur.lastrowid
    return id

def insert_method(name):
    request = 'Select * from ' + table_evaluation_name +' where name = ?;'
    conn = create_connection(location())
    id = 0
    with conn:
        cur = conn.cursor()
        cur.execute(request, (name,))
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute('insert into ' + table_evaluation_name +'(name) values (?);', (name, ))
            id = cur.lastrowid
        else:
            id = rows[0][0]
    return id

def insert_data(data, config_id):
    conn = create_connection(location())
    id = 0
    with conn:
        cur = conn.cursor()
        cur.execute('insert into ' + table_datensatz_name +'(config_id, Werte) values (?, ?);', (config_id, data))
        id = cur.lastrowid
    return id

def insert_cross(method_id, data_id, result_id):
    conn = create_connection(location())
    id = 0
    with conn:
        cur = conn.cursor()
        cur.execute('insert into ' + table_cross_name +'(data_id, result_id, method_id) values (?,?,?);', (method_id, data_id, result_id))
        id = cur.lastrowid
    return id