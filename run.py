from flask_api import create_app, db
from flask_api.entities.dog import Dog
from flask_migrate import Migrate

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Dog": Dog}


migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
