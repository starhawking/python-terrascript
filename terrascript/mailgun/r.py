from terrascript import Resource
class mailgun_domain(Resource):
    def __init__(self, _label, **kwargs): super().__init__('mailgun_domain', _label, **kwargs)
domain = mailgun_domain

