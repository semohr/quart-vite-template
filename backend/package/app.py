"""Quart application.

Definition and functions to create and configure the quart
app.
"""

import os
from pprint import pformat

from quart import Quart


def create_app():
    """Create and configure the Quart application.

    This function initializes the Quart app with necessary configurations,
    sets up database connections, registers blueprints, and initializes
    various services such as websockets, terminal management, disk inboxes,
    and tag deletion. It also ensures that exceptions are propagated correctly
    and configures CORS for development purposes.

    Parameters
    ----------
    mode : str
        The mode in which the app is running. Defaults to "dev".

    Returns
    -------
    app : Quart
        The configured Quart application instance.
    """
    app = Quart(__name__, instance_relative_config=True)

    # TODO: load config
    # app.config.from_object(switch[mode])

    # Setup all routes
    from .routes import api_bp

    app.register_blueprint(api_bp)

    # Print out the config
    config = {key: value for key, value in app.config.items()}
    # log.debug(f"App created with config: \n {pformat(config)}")

    return app
