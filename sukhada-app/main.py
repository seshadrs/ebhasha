from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == "POST":
    	src = request.form['source-text']
        results = translate_text(src)
    return render_template('index.html', results=results)

def translate_text(txt):
	results = []
	url_tam = URL_TEMPLATE % (txt, ENGLISH, TAMIL)
	url_mar = URL_TEMPLATE % (txt, ENGLISH, MARATHI)
	url_eng = URL_TEMPLATE % (txt, ENGLISH, HINDI)
	results.append(get_translate(url_tam))
	results.append(get_translate(url_mar))
	results.append(get_translate(url_eng))
	return results

def get_translate(url):
	r = requests.request('GET', url)
	resp = json.loads(r.content)
	res = resp['data']['translations'][0]['translatedText']
	return res

URL_TEMPLATE="https://www.googleapis.com/language/translate/v2?key=AIzaSyCWzGMSyNdUyAU1FnayuzsShmSlxXcQDGI&q=%s&source=%s&target=%s"
MARATHI = "mr"
TAMIL = "ta"
HINDI = "hi"
ENGLISH = "en"


if __name__ == "__main__":
    app.run()
