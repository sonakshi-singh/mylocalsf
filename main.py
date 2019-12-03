from flask import Flask, render_template  
from .extensions import db, login_manager    
def create_app(config_file='settings.py'):
	app = Flask(__name__)

	app.config.from_pyfile(config_file )

	db.init_app(app)

	login_manager.init_app(app)

	#login_manager.login_view=''
	#login_manager.user_loader
	#def load_user(user_id):
		#return User.query.get(user_id)



	return app 

@app.route("/")
def home():
    return render_template("index.html")


    

    
if __name__ == "__main__":
    app.run()
  