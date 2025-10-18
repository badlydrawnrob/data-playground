"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

from piccolo.conf.apps import AppConfig
from fruits.tables import Fruits


APP_CONFIG = AppConfig(
    app_name="fruits",
    table_classes=[Fruits], # Explicitly list all tables here
    migrations_folder_path=None, #! `None` not currently supported
    migration_dependencies=[], # Optional
    commands=[] # Advanced use only
)
