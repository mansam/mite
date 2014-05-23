def not_found(environ, start_response):
    """
    Called if no URL matches.

    """

    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

def internal_server_error(environ, start_response):
    """
    Called if an unexpected exception occurs.

    """

    start_response('500 INTERNAL SERVER ERROR', [('Content-Type', 'text/plain')])
    return ['500 Internal Server Error']