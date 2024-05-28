from django.apps import AppConfig
from flask import Flask, render_template, request, redirect, url_for
from transbank.webpay.webpay_plus.transaction import Transaction

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    
app = Flask(__name__)

# Credenciales de prueba proporcionadas por Transbank
commerce_code = '597055555532'
api_key = 'YourAPIKeyHere'  # Cambia esto por la API Key de prueba proporcionada por Transbank

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagar', methods=['POST'])
def pagar():
    amount = request.form['amount']
    session_id = 'mi_sesion'
    buy_order = 'orden_compra_' + str(int(amount))
    return_url = url_for('retorno', _external=True)

    response = Transaction.create(buy_order, session_id, amount, return_url)
    
    if response.response_code == 0:
        return redirect(response.url + '?token_ws=' + response.token)
    else:
        return 'Error en la transacción: ' + str(response.response_code)

@app.route('/retorno')
def retorno():
    token = request.args.get('token_ws')
    response = Transaction.commit(token)

    if response.response_code == 0:
        return render_template('resultado.html', response=response)
    else:
        return 'Error en la transacción: ' + str(response.response_code)

if __name__ == '__main__':
    app.run(debug=True)
