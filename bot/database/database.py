import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """
	Create a database connection to a SQLite database

	:param db_file: database file
	:return: Connection object or None
	"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite3 database (version {sqlite3.version})")
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """
	Create a table from the create_table_sql statement

	:param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_tournament(conn, tournament):
	"""
	Create a new tournament in the tournaments database

	:param conn:
    :param project:
    :return: project id
	"""
	sql = ''' INSERT INTO tournaments(g_id,t_name,t_type,t_url,t_challonge_id,t_creator_id,t_status)
              VALUES(:guild,:name,:type,:url,:id,:creator,:status) '''
	cur = conn.cursor()
	cur.execute(sql, tournament)
	conn.commit()
	return cur.lastrowid

def execute_request(conn, sql, data=None):
	cur = conn.cursor()

	if data is not None:
		cur.execute(sql, data)
	elif  data is None:
		cur.execute(sql)

	return cur.fetchall()
