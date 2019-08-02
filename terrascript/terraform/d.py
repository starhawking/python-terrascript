from terrascript import Data


class terraform_remote_state(Data):
    def __init__(self, _label, **kwargs):
        super().__init__('terraform_remote_state', _label, **kwargs)


remote_state = terraform_remote_state
