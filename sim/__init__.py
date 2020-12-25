from flask import Flask


app=Flask('__name__', template_folder='sim/templates', static_folder='sim/static' )
app.config['SECRET_KEY']="iboibo"

from sim.mahasiswa.routes import rmahasiswa
app.register_blueprint(rmahasiswa)