import os
from bottle import route, run, response
from horoscope import generate_prophecies

@route("/api/forecasts")
def forecasts():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Content-Type'] = 'application/json'
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