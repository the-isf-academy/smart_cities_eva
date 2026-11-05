# to run the server: 
# # flask --app app.py --debug run

from flask import Flask, request, render_template, url_for, redirect, request
from models import db, Courts  
import secrets

app = Flask(__name__, static_url_path=f'/')
app.secret_key = secrets.token_hex(32)  # Required for CSRF protection
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

# Link the db to this specific app
db.init_app(app)

# Create the tables if it does not exisit, ignore if it exists 
with app.app_context():
    db.create_all()


@app.route(f"/", methods=['GET'])
def index():
    courts = db.session.scalars(db.select(Courts)).all()
    print(courts)

    return render_template(
        'index.html',
        courts = courts)



if __name__ == '__main__': 
    app.run(debug=True, port=5000)

    
