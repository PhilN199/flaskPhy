from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch('127.0.0.1', port=9200)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search():
    search_term = request.form["input"]
    res = es.search(
        index="nsdl",
        size=100,
        body={
            "query": {
                "multi_match" : {
                    "query": search_term,
                    "fields": [
                        "CR_ID","CR_OAI_IDENTIFIERS","CR_NATIVE_ID","CR_TITLE","CR_CREATE_DATE","CR_AUTHOR_NAME","CR_PROVIDER","CR_PROVIDER_ABSTRACT","CR_OERC_URL","CR_URL","CR_SUBJECT","CR_MATERIAL_TYPE","CR_MEDIA_FORMATS","CR_LEVEL","CR_SUBLEVEL","CR_GRADE","CR_ABSTRACT","CR_KEYWORDS","CR_ED_STANDARDS","CR_ACCESSIBILITY","CR_HTTP_STATUS","CR_DOI_HANDLE"
                    ]
                }
            }
        }
    )
    return render_template('results.html', res=res )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
