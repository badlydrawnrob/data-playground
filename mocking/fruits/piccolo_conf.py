# ------------------------------------------------------------------------------
# Piccolo configuration file.
# ==============================================================================
# > @ https://piccolo-orm.com/docs/configuration/

from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine


DB = SQLiteEngine(path='fruits.sqlite', log_queries=True, log_responses=True)

APP_REGISTRY = AppRegistry(
    apps=["fruits.piccolo_app", "piccolo_admin.piccolo_app"]
)
