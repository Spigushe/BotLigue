# Tournaments's table
sql_create_tournaments_table = """
	CREATE TABLE IF NOT EXISTS tournaments (
		g_id BIGINT,
		t_id INTEGER,
		t_name VARCHAR(255),
		t_type VARCHAR(255),
		t_url VARCHAR(255),
		t_challonge_id INTEGER,
		t_creator_id BIGINT,
		t_status INT,
		PRIMARY KEY(t_id AUTOINCREMENT)
	);
"""

# Sample tournament
sample_tournament = {
	"guild": 0,
	"name": "",
	"type": "",
	"url": "",
	"id": 0,
	"creator": 0,
	"status": 0
}
