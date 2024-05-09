from flask import Flask, render_template
from flask import g
from flask import jsonify,request
from flask_cors import CORS
import sqlite3


DATABASE = 'rockrBlog.db'


app = Flask(__name__)

CORS(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paginaPrincipal')
def cargaPrincipa():
    cur = get_db().cursor()
    cur.execute('SELECT * FROM news')
    noticias=cur.fetchall()
    return jsonify(noticias)

@app.route('/articulo',methods=['POST'])
def cargaArticulo():
    cur = get_db().cursor()
    titulo = request.form.get('titulo')
    print(titulo)
    query='SELECT fecha, artista, imagen, articulo FROM news WHERE titulo = "'+titulo+'"' 
    cur.execute(query)
    info=cur.fetchone()
    articulo =render_template('article.html',
                              fecha=info[0],
                              artista=info[1],
                              imagen=info[2],
                              articulo=info[3],
                              titulo=titulo)
    return articulo


@app.route('/contacto',methods=['POST'])
def contacto():
    cur = get_db().cursor()
    name = request.form.get('nombre')
    email = request.form.get('email')
    phone = request.form.get('phone')
    post = request.form.get('post')
    query='INSERT INTO cotact(name, email, phone, post)\
         Values('+name+','+email+','+phone+','+post+') '
    cur.execute(query)
    get_db().commit()
    return "Oki Doki"
