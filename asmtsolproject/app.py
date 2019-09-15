from flask import Flask, request, render_template
import wikipedia

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return render_template("home.html")
    else :
        to_search = request.form.get('search_string')
        try:
            ret = wikipedia.search(to_search, results=3)[0]
            pg = wikipedia.page(ret,auto_suggest=True)
            title = pg.title
            url = pg.url
            summ = wikipedia.summary(ret,auto_suggest=True)
        except :
            help = "An error was thrown as the search term is not common. Please return to the home page and try another simpler search term."
            return render_template("display.html", title="Error detected", url="Not found", summary=help)
        else :
            return render_template("display.html", title=title, url=url, summary=str(summ))

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)