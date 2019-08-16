from terrascript import Resource
class librato_space(Resource):
    def __init__(self, _label, **kwargs): super().__init__('librato_space', _label, **kwargs)
space = librato_space

class librato_space_chart(Resource):
    def __init__(self, _label, **kwargs): super().__init__('librato_space_chart', _label, **kwargs)
space_chart = librato_space_chart

class librato_metric(Resource):
    def __init__(self, _label, **kwargs): super().__init__('librato_metric', _label, **kwargs)
metric = librato_metric

class librato_alert(Resource):
    def __init__(self, _label, **kwargs): super().__init__('librato_alert', _label, **kwargs)
alert = librato_alert

class librato_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('librato_service', _label, **kwargs)
service = librato_service

