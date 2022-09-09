from mysql import connector

def test_db():
	conn = connector.connect(
		host="172.18.0.1",
		port=3306,
		user="root",
		password="daswid",
		database="crowbase"
	)

	cur = conn.cursor()
	cur.execute("SELECT * FROM crow")

	assert len(cur.fetchall()) > 0
