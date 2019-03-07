import os
from bottle import route, run
from horoscope import generate_prophecies

@route("/api/forecasts")
def forecasts():
	return {"prophecies" : generate_prophecies(total_num = 6, num_sentences = 2), }	

	
if os.environ.get('APP_LOCATION') == 'heroku':
	run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
	run(host='localhost', port=8080, debug=True)

# run(
# 	host="localhost",
# 	port=8080,
# 	autoreload=True
# )