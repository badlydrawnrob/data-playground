from piccolo.engine.sqlite import SQLiteEngine


# You'd probably want to set `connection_kwargs` for production use
DB = SQLiteEngine(path='fruits.sqlite', log_queries=True, log_responses=True)
