
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1 style="color: red;text-align: center">hello,world!!!</h1>']
