import flask
from flask import request, jsonify, abort

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hey World</h1>"

@app.route('/api/companies/copyrighted', methods=['POST'])
def add_copyright_symbol():
    if not request.json or not 'input' in request.json:
        abort(400)
    else:
        userinput = request.json['input']
        companies = ['Oracle', 'Google', 'Microsoft', 'Amazon', 'Deloitte']

        for company in companies:
            if company in userinput:
                userinput = userinput.replace(company, company + '©')
                return jsonify(userinput), 201

app.run()