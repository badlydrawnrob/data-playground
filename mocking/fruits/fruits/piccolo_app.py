"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG. Some functions (like auto migrations) aren't supported with
SQLite. `table_classes=` can also be explicitly listed by importing the tables
and using a `List Table`.

Security
--------
> Database settings should be secret

1. Never commit secrets to Github!
2. Store all passwords, keys, secrets, etc privately!
3. Consider tooling for `.env` settings (DevBox, etc)

Settings
--------
> Pydantics settings documentation is shitty and confusing. Find a better and
> easier way to achieve this (without needing OS path etc).

#! Currently using `python-decouple`. As our `piccolo_app` file is in a subfolder,
we need to use `RepositoryEnv`. Using in the root folder is easier.

1. Pydantic settings
    - @ https://docs.pydantic.dev/2.10/migration/#basesettings-has-moved-to-pydantic-settings
    - @ https://docs.pydantic.dev/latest/concepts/pydantic_settings/#nested-model-default-partial-updates
2. Python decouple
    - Seems to have the fewest dependencies
    - @ https://pypi.org/project/python-decouple/
    - @ https://youtu.be/0_seNFCtglk?t=1282
3. Environs
    - @ https://pypi.org/project/environs/
4. Avoid relying on `.env` files
    - @ https://tinyurl.com/a-note-on-env-security
"""

from decouple import config
from piccolo.conf.apps import AppConfig, table_finder


APP_CONFIG = AppConfig(
    app_name="fruits",
    table_classes=table_finder(modules=['fruits.tables']), # ... Or `List Table`
    migrations_folder_path=None, #! `None` not currently supported
    migration_dependencies=[], # Optional
    commands=[] # Advanced use only
)

SECRET = config("SECRET_KEY") #! Should be named `SECRET_KEY`?