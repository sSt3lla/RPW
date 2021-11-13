from app import create_app
from app import cli

app = create_app()
cli.register(app)