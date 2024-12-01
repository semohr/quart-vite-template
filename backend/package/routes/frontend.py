"""The glue between quart and vite.

The frontend blueprint allows to host a precompiled
vite application as a quart route. This is done for
simplicity in the production environment as running
multiple servers has some impact on performance
and image size.

For more complicated it is always possible to remove
the integration in favour for a other server or a
reverse proxy such as nginx.
"""

from quart import Blueprint, send_from_directory

frontend_bp = Blueprint("frontend", __name__)


@frontend_bp.route("/", defaults={"path": "index.html"})
@frontend_bp.route("/<path:path>")
def reverse_proxy(path):
    """Frontend catch all.

    Catches all request on all paths not defined in
    other blueprints.
    Basically acts as a reverse proxy for the frontend.
    """
    # not include assets
    if (
        not "assets" in path
        and not "logo.png" in path
        and not path.startswith("favicon.ico")
    ):
        path = "index.html"

    # Remove everything infront of assets
    if "assets" in path:
        path = path[path.index("assets") :]
    if "logo.png" in path:
        path = path[path.index("logo.png") :]

    r = send_from_directory("../../frontend/dist/", path)
    return r
