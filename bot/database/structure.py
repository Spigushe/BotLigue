# Tournaments's table
sql_create_tournaments_table = """
	CREATE TABLE IF NOT EXISTS tournaments (
		id_tournament INTEGER,
		guild_id BIGINT,
		tournament_name VARCHAR(255),
		tournament_type VARCHAR(255),
		tournament_url VARCHAR(255),
		tournament_challonge_id INTEGER,
		tournament_creator_id BIGINT,
		tournament_status INT,
		PRIMARY KEY(id_tournament AUTOINCREMENT)
	);
"""

# Sample tournament
table_tournament_sample = {
	"guild": 123,
	"name": "test",
	"type": "round robin",
	"url": "er",
	"id": 123,
	"creator": 123,
	"status":1
}
