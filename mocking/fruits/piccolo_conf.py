# ------------------------------------------------------------------------------
# Piccolo configuration file.
# ==============================================================================
# > @ https://piccolo-orm.com/docs/configuration/
#
# Python decouple
# ---------------
# We can set a default value for production, and make sure the type is set. By
# default `python-decouple` treats values as strings.

from decouple import config
from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine


#! Remember that query logs are NOT responses
LOG_QUERIES = config("SQLITE_LOG_QUERIES", default=False, cast=bool)
LOG_RESPONSES = config("SQLITE_LOG_RESPONSES", default=False, cast=bool)


DB = SQLiteEngine(path='fruits.sqlite', log_queries=LOG_QUERIES, log_responses=LOG_RESPONSES)

APP_REGISTRY = AppRegistry(
    apps=["fruits.piccolo_app", "piccolo.apps.user.piccolo_app"]
)
