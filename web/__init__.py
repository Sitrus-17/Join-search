from flask import (Flask, render_template)

def create_app():
    app = Flask(__name__)
    
    @app.route('/test')
    def test():
        return render_template("test1.html")
    
    return app