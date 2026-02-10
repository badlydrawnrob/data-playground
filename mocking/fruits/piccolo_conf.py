# ------------------------------------------------------------------------------
# Piccolo configuration file.
# ==============================================================================
# > @ https://piccolo-orm.com/docs/configuration/
#
# Python decouple
# ---------------
# We can set a default value for production, and make sure the type is set. By
# default `python-decouple` treats values as strings.
#
# Notes
# -----
# 1. Remember that query logs are NOT responses!

from decouple import config
from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine


DATABASE = config("SQLITE_DATABASE", default="fruits.sqlite")
LOG_QUERIES = config("SQLITE_LOG_QUERIES", default=False, cast=bool) #! (1)
LOG_RESPONSES = config("SQLITE_LOG_RESPONSES", default=False, cast=bool)


DB = SQLiteEngine(path=DATABASE, log_queries=LOG_QUERIES, log_responses=LOG_RESPONSES)

APP_REGISTRY = AppRegistry(
    apps=["fruits.piccolo_app", "piccolo.apps.user.piccolo_app"]
)
