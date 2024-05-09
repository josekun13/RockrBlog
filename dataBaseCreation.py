import sqlite3

#conexion
con = sqlite3.connect("rockrBlog.db")
cur = con.cursor()

#Tabla news feed
cur.execute("CREATE TABLE news(id INTEGER NOT NULL PRIMARY KEY ,titulo TEXT, artista TEXT, contenido TEXT , imagen TEXT, articulo TEXT, fecha TEXT)")

#Tabla contact
cur.execute("CREATE TABLE contact(name TEXT NOT NULL PRIMARY KEY ,email TEXT, phone TEXT, post TEXT)")


#llenar Tabla news
cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(1 ,'titulo1',\
            'artista1','contenido1',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(2 ,'titulo2',\
            'artista2','contenido2',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(3 ,'titulo3',\
            'artista3','contenido3',\
            '#',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(4 ,'titulo4',\
            'artista4','contenido4',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(5 ,'titulo5',\
            'artista5','contenido5',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(6 ,'titulo6',\
            'artista6','contenido6',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(7 ,'titulo7',\
            'artista7','contenido7',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(8 ,'titulo8',\
            'artista8','contenido8',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(9 ,'titulo9',\
            'artista9','contenido9',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(10 ,'titulo10',\
            'artista10','contenido10',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

cur.execute("INSERT INTO news(id, titulo, artista, \
            contenido, imagen, articulo, fecha) VALUES(11 ,'titulo11',\
            'artista11','contenido11',\
            'https://media.istockphoto.com/id/1319479588/es/foto/los-m%C3%BAsicos-tocaban-m%C3%BAsica-rock-en-el-escenario-hab%C3%ADa-un-p%C3%BAblico-lleno-de-gente-viendo-el.jpg?s=612x612&w=0&k=20&c=H1kP1pyY2dXgaYHzIkBrGSaTCqR1ukUuT4AXS1T2QpQ=',\
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
             Donec id odio at risus sagittis convallis. Quisque vitae \
            purus ac sem tempor dignissim nec lacinia elit. Maecenas \
            tincidunt a urna nec cursus. Mauris viverra facilisis lectus,\
             non mattis dolor rhoncus vel. Aliquam erat volutpat. Integer \
            faucibus justo in tortor accumsan, sit amet ultricies nulla \
            dictum. Cras mattis nulla a metus lobortis venenatis. Nam \
            non tincidunt nisi. Suspendisse ornare convallis finibus.\n \
            Praesent iaculis dignissim orci, quis pharetra tortor blandit\
             a. Duis quis turpis id odio tempus ultricies id et tellus.\
             Vivamus scelerisque libero quam, eu imperdiet tellus aliquet \
            ac. Aenean laoreet dolor vel mollis dictum. Vivamus semper \
            suscipit lorem, vel bibendum enim gravida eget. Curabitur id \
            nunc massa. Aenean rutrum iaculis velit, eget feugiat sem \
            vulputate id. Nullam quis scelerisque libero. Ut sit amet nibh \
            condimentum, cursus est quis, porttitor nulla. Praesent ornare \
            nulla ac justo pretium lacinia ac et leo.\n \
            Mauris fermentum dui ut placerat euismod. Praesent augue enim,\
             aliquam id varius non, elementum id neque. Praesent vel \
            imperdiet felis. Pellentesque suscipit tempor nulla eget \
            malesuada. Sed orci nunc, suscipit ut laoreet a, consequat \
            non magna. Pellentesque malesuada augue sit amet odio sagittis \
            semper. Sed consectetur nibh non augue efficitur mollis. Fusce \
            laoreet a ex vel fringilla. Morbi a congue ante. Cras convallis \
            risus a volutpat lobortis. Cras ac luctus mauris. Fusce auctor \
            in urna ornare viverra. ',\
            'Jan 6 2018')")

con.commit()