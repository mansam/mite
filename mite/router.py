from httperrors import not_found, internal_server_error
from webob import Request

class WSGIRouter(object):

	def __init__(self, debug=False):
		self.routes = {}
		self.debug = debug

	def add_route(self, path, handler):
		self.routes[path] = handler

	def dispatch(self, environ, start_response):
		"""
		Dispatch incoming requests to the appropriate
		handler.

		"""

		try:
			req = Request(environ)

			path = environ.get('PATH_INFO', '').lstrip('/')
			path = _prep_path(path)

			for route, cb in self.routes.items():
				if self.debug:
					print(route, path)
				if _match_path(route, path):
					val = cb(start_response, req, **_parse_path(route, path))
					if self.debug:
						print(val)
					return val
				else:
					if self.debug:
						print("No match", route, path)

			return not_found(environ, start_response)
		except:
			if self.debug:
				import traceback
				traceback.print_exc()
			return internal_server_error(environ, start_response)
		else:
			return not_found(environ, start_response)

	def __call__(self, *args, **kwargs):
		return self.dispatch(*args, **kwargs)

def _match_path(route, path):
	if len(route) != len(path):
		return False

	for i, elem in enumerate(route):
		if not elem.startswith(':'):
			if route[i] != path[i]:
				return False
	return True

def _prep_path(path):
	return tuple(path.strip('/').split('/'))

def _parse_path(route, path):
	params = {}

	if len(route) != len(path):
		raise ValueError("Path does not match route.")

	for i, elem in enumerate(route):
		if elem.startswith(':'):
			params[elem[1:]] = path[i]

	return params
