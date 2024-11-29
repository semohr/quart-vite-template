"""Register all route blueprints."""

from quart import Blueprint

from .example import example_bp

api_bp = Blueprint("api_v1", __name__, url_prefix="/api_v1")

# Register all nested blueprints here
# at the moment that is only the example
# but you may add more here if wanted.
api_bp.register_blueprint(example_bp)

__all__ = ["api_bp"]
