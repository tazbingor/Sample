#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager
from werkzeug.utils import secure_filename
from app import create_app, db

app = create_app()
manager = Manager(app)


@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)


@manager.command
def test():
    pass


@manager.command
def deploy():
    pass

# if __name__ == '__main__':
#     # app.debug = True
#     # app.run(debug=True)
#     # manager.run()
#     dev()
