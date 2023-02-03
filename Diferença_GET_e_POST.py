from flask import Flask, session, request, jsonify

app = Flask("Servidor API da ITsafe", static_url_path='')
app.secret_key ='ajsd8h218hd8hcs8hj9219ejd9ch8mc91u239m921cvu39du2191jd'


@app.route('/api/visitas', methods=['post'])
def test():
   senha =  request.form["senha"] # usuario vai enviar os dados
   success = False
   if senha == "123": # caso a senha seja realmente 123 mude para True
      success = True


   return jsonify({"success":success})  # Retorna os Dados no formato Json



debug = True

app.run(host='0.0.0.0',port=1337,debug=debug)
