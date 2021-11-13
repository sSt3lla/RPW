from app import create_app, cli, db
#Needed for database to get a referance and shell context
from app.models import User 

app = create_app()
cli.register(app)

#Nicer when on the shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}