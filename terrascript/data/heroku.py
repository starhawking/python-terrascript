# terrascript/data/heroku.py
import terrascript


class heroku_addon(terrascript.Data):
    pass


class heroku_app(terrascript.Data):
    pass


class heroku_pipeline(terrascript.Data):
    pass


class heroku_space(terrascript.Data):
    pass


class heroku_space_peering_info(terrascript.Data):
    pass


class heroku_team(terrascript.Data):
    pass


__all__ = [
    "heroku_addon",
    "heroku_app",
    "heroku_pipeline",
    "heroku_space",
    "heroku_space_peering_info",
    "heroku_team",
]
