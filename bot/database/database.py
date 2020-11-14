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
	sql = ''' INSERT INTO tournaments(guild_id,tournament_name,tournament_type,tournament_url,tournament_challonge_id,tournament_creator_id)
              VALUES(:guild,:name,:type,:url,:id,:creator) '''
	cur = conn.cursor()
	cur.execute(sql, tournament)
	conn.commit()
	return cur.lastrowid
