from flask import Flask, send_from_directory

app = Flask(__name__)

# A rota que você deve acessar é exatamente esta: '/cotacao'
@app.route('/cotacao/')
def servir_imagem_cotacao():
    # Esta função busca o arquivo 'cotacao_atual.png'
    # DENTRO da pasta 'imagens_publicas'
    return send_from_directory('imagens_publicas', 'cotacao_atual.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)