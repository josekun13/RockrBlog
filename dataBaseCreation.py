import sqlite3

#conexion
con = sqlite3.connect("rockrBlog.db")
cur = con.cursor()

#Tabla news feed
cur.execute("CREATE TABLE news(id INTEGER NOT NULL PRIMARY KEY ,titulo TEXT, artista TEXT, contenido TEXT , imagenTEXT)")

#Tabla articulo
cur.execute("CREATE TABLE articulos(id INTEGER NOT NULL PRIMARY KEY ,contenido TEXT , noticia INTEGER NOT NULL, FOREIGN KEY (noticia) REFERENCES news (id) )")