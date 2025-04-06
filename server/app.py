# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def view(id):
    
    earthquake = db.session.get(Earthquake,id)
    
    if not earthquake:
        return {"message": f"Earthquake {id} not found."}, 404
    
    
    earthquake_dict = earthquake.to_dict()
    
   
    return earthquake_dict, 200

@app.route('/earthquakes/magnitude/<float:magnitude>') 
def view_magnitude(magnitude):
     
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    
    quakes_list = [quake.to_dict() for quake in quakes]

    
    response = {
        "count": len(quakes_list),
        "quakes": quakes_list
    }

    return response, 200   



if __name__ == '__main__':
    app.run(port=5555, debug=True)
