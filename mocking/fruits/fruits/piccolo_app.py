# ------------------------------------------------------------------------------
# Fruits app: settings
# ==============================================================================
# > See `badlydrawnrob/python-playground/building-with-fast-api` for docs.

from decouple import config
from fruits.tables import Colors, Fruits
from piccolo.conf.apps import AppConfig


APP_CONFIG = AppConfig(
    app_name="fruits",
    table_classes=[Colors, Fruits],
    migrations_folder_path=None,
    migration_dependencies=[],
    commands=[]
)

SECRET = config("SECRET_KEY")