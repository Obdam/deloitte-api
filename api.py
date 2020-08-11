import flask
from flask import request, jsonify, abort

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/home', methods=['GET'])
def home():
    return "<h1>Hey World</h1>"

# A route to return all of the available entries in our catalog.
@app.route('/api/companies/copyrighted', methods=['POST'])
def add_copyright_symbol():
    if not request.json or not 'input' in request.json:
        abort(400)

userinput = request.json['input']
companies = ['Oracle', 'Google', 'Microsoft', 'Amazon', 'Deloitte']

for company in companies:
    if company in userinput:
        userinput = userinput.replace(company, company + '©')
        # print(userinput) 


app.run()