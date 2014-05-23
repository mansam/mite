import router
import httperrors

def handler(content_type):
    def handler_h(f):
        def inner(start_response, request, **params):
            try:
                resp = f(request, **params)
                start_response('200 OK', [('Content-Type', content_type)])
                return resp
            except:
                return httperrors.internal_server_error(environ, start_response)
        return inner
    return handler_h
