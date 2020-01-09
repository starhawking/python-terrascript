import terrascript
import terrascript.provider
import terrascript.resource

# *** These test work but terrascript.Locals is not supported. ***

class TestLocals(object):

    def __init__(self):
        self.cfg = terrascript.Terrascript()
        self.cfg += terrascript.provider.aws(region='us-east-1')

    def test_locals_added_once(self):

        self.cfg += terrascript.Locals(service_name="forum", owner="Community Team")

        assert self.cfg['locals']['service_name'] == 'forum'
        assert self.cfg['locals']['owner'] == 'Community Team'

        #assert self.cfg.locals.service_name == 'forum'
        #assert self.cfg.locals.ower == 'Community Team'

    def test_locals_added_twice(self):

        self.cfg += terrascript.Locals(service_name="forum")
        self.cfg += terrascript.Locals(owner="Community Team")

        assert self.cfg['locals']['service_name'] == 'forum'
        assert self.cfg['locals']['owner'] == 'Community Team'
