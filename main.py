from flask import Flask, render_template  

app=Flask(__name__)

	

@app.route("/")
def home():
    return render_template("index.html")
@main.route('/rmain')
def rmain():
    return render_template("rmain.html")

    
if __name__ == "__main__":
    app.run()
  