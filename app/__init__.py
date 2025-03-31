from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

mysql = MySQL()

def create_app():
    # Configuração de caminhos
    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    app = Flask(__name__,
               template_folder=os.path.join(base_dir, 'templates'),
               static_folder=os.path.join(base_dir, 'static'))
    
    # Configurações
    app.config.update({
        'SECRET_KEY': os.getenv('SECRET_KEY') or 'fallback_secret_key',
        'MYSQL_HOST': '157.230.233.182',
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': '2899956Hg@nhm',
        'MYSQL_DB': 'banco_linha',
        'MYSQL_PORT': 3306,  # Se você estiver usando a porta padrão do MySQL
        'MYSQL_CURSORCLASS': 'DictCursor',
        'UPLOAD_FOLDER': os.path.join(base_dir, 'uploads'),
        'MAX_CONTENT_LENGTH': 16 * 1024 * 1024  # 16MB
    })

    # Cria pasta de uploads se não existir
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Inicializa o MySQL
    mysql.init_app(app)
    
    # Registrando Blueprints
    from . import routes, auth
    app.register_blueprint(routes.main_bp)
    app.register_blueprint(auth.auth_bp)

    return app
