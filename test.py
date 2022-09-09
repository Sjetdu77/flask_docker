from mysql import connector
import requests

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

def test_site():
	r = requests.get('http://172.18.0.1:5000/')
	assert r.status_code == 200