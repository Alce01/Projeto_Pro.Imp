import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory, jsonify
from website import app

UPLOAD_FOLDER = './data'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        # verifique se a solicitacao de postagem tem a parte do arquivo
        if 'file' not in request.files:
            flash('Nao tem a parte do arquivo')
            return redirect(request.url)
        file = request.files['file']
        
        # Se o usuario nao selecionar um arquivo, o navegador envia um
        # arquivo vazio sem um nome de arquivo.