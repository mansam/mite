from validator import validate, Equals, Required
import mite.router

class TestWSGIRouter(object):

    def test_route_parser(self):

        test_path = ("packages", "validator.py", "0.8.0")
        route = ("packages", ":pkg", ":ver")

        params = mite.router.parse_path(route, test_path)
        validation = {
            "pkg": [Required, Equals("validator.py")],
            "ver": [Required, Equals("0.8.0")]
        }
        valid, errs = validate(validation, params)
        assert errs == {}

    def test_match_route(self):
        routes = [
            (('packages'), 1),
            (('packages', ':pkg_name'), 2),
            (('packages', ':pkg_name', ':ver', ':dist_file'), 4),
            (('packages', ':pkg_name', ':dist_file'), 3),
        ]
        test_path = ("packages", "validator.py", "0.8.0")
        assert not mite.router.match_path(routes[0][0], test_path)
        assert not mite.router.match_path(routes[1][0], test_path)
        assert not mite.router.match_path(routes[2][0], test_path)
        assert mite.router.match_path(routes[3][0], test_path)


