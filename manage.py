from app import create_app
from flask_script import Manager, Server


# Creating app instance
app = create_app()

manager = Manager(app)
manager.add_command('runserver', Server(use_debugger= True))



if __name__ == '__main__':
    manager.run()