from flask import Flask, render_template

app = Flask("ITsafe API Server",static_url_path='')


@app.route('/https://desafios.cysource.com.br/PYTHON/stage1.php', methods=['POST'])
def ola_mundo():
    return render_template('stage1.php')


debug = True
app.run(host='0.0.0.0', port=1337, debug=debug)
