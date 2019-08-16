from terrascript import Data
class heroku_addon(Data):
    def __init__(self, _label, **kwargs): super().__init__('heroku_addon', _label, **kwargs)
addon = heroku_addon

class heroku_app(Data):
    def __init__(self, _label, **kwargs): super().__init__('heroku_app', _label, **kwargs)
app = heroku_app

class heroku_space(Data):
    def __init__(self, _label, **kwargs): super().__init__('heroku_space', _label, **kwargs)
space = heroku_space

class heroku_space_peering_info(Data):
    def __init__(self, _label, **kwargs): super().__init__('heroku_space_peering_info', _label, **kwargs)
space_peering_info = heroku_space_peering_info

class heroku_team(Data):
    def __init__(self, _label, **kwargs): super().__init__('heroku_team', _label, **kwargs)
team = heroku_team

