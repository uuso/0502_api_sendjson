from bottle import route, run
from horoscope import generate_prophecies

@route("/api/forecasts")
def forecasts():
	return {"prophecies" : generate_prophecies(total_num = 6, num_sentences = 2), }	

run(
	host="localhost",
	port=8080,
	autoreload=True
)
