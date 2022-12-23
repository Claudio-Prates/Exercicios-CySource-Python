from flask import Flask, session, jsonify

app = Flask("Servidor API da ITsafe", static_url_path='')
app.secret_key ='ajsd8h218hd8hcs8hj9219ejd9ch8mc91u239m921cvu39du2191jd'


@app.route('/api/visitas', methods=['GET'])
def test():
    if session.get("visitas"):  # se o usuario já estiver conectado mais de uma vez
       session["visitas"] += 1  # aumenta em 1 o numero de visitas
    else:
       session["visitas"] = 1  # caso contrario, caso seja a primeira vez que o usuario está entrando, coloque 1

    return jsonify({"visitas":session["visitas"]}) # Retorna os Dados no formato Json


debug = True

app.run(host='0.0.0.0 ,port=1337,debug=debug)
