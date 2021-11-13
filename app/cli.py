import click, os

def register(app):
    #Adds custom command line functionality

    @app.cli.command("add-module")
    @click.argument("name")
    def create_module(name):
        """Creates a blueprint structure

    Creates a blueprint structure with NAME and fills in with, Templates, __init.py, routes.py
    """
        try:
            os.mkdir(name)
        except FileExistsError:
            print(f"Error ({name}) already exists")
            return
        os.chdir(name)
        os.mkdir("Templates")

        with open('__init__.py', 'w+') as f:
            f.write(f'''from flask import Blueprint
bp = Blueprint('{name}', __name__)
from .{name} import routes
                    ''')
        
        with open('routes.py', 'w+') as f:
            f.write(f'''from ..{name} import bp
                    ''')