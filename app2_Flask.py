from flask import Flask, session, jsonify, request, render_template

app = Flask("Servidor API da ITsafe", static_url_path='')
app.secret_key ='ajsd8h218hd8hcs8hj9219ejd9ch8mc91u239m921cvu39du2191jd'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/visitas', methods=['GET'])
def test():
    senha = request.args.get("senha")
    success = False
    if senha == "123":
        success = True

    return jsonify({'success': success})

debug = True

app.run(host='0.0.0.0', port=1337, debug=debug)
