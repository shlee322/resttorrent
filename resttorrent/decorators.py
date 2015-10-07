import json
from functools import wraps
from flask import request
from resttorrent.app import app
from resttorrent.exceptions import APIException


def command(version, url, method='GET', command_name=None):
    def decorator(f):
        name = command_name if command_name else f.__name__

        # Flask
        @wraps(f)
        def flask_command(*args, **kwargs):
            func_argv = f.func_code.co_varnames[:f.func_code.co_argcount]

            new_kwargs = {}

            def copy_kwargs(data):
                if not data:
                    return

                for name in func_argv:
                    if data.get(name):
                        new_kwargs[name] = data.get(name)

            # Copy Request Query
            copy_kwargs(request.args)

            # Copy Request Body (Form)
            copy_kwargs(request.form)

            # Copy Request Body (File)
            copy_kwargs(request.files)

            # Copy Request Body (Json)
            copy_kwargs(request.get_json())

            # Copy Request URL Var
            copy_kwargs(kwargs)

            try:
                result = f(**new_kwargs)
                if not result.get('status'):
                    result['status'] = 'success'
                result = json.dumps(result)
            except APIException, e:
                result = json.dumps({
                    'status': 'fail',
                    'error': {
                        'code': e.error_code,
                        'message': e.message
                    }
                })

            mime_type = 'application/json'
            callback = request.args.get('callback', False)
            if callback:
                # if jsonp
                result = str(callback) + '(' + result + ')'
                mime_type = 'application/javascript'

            resp = app.response_class(result, mimetype=mime_type)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        app.add_url_rule('/v%s%s' % (version, url), name, flask_command, methods=[method])

        # Socket.IO
        @wraps(f)
        def socketio_command():
            result = f()
            return result

        return f

    return decorator
