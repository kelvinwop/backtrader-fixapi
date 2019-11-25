import quickfix as fix

from api.pricing import FixPricing

class FixPricingClient():
    def __init__(self, config_file='../config/pricing.conf', username = '', password = ''):
        self.config_file = config_file
        self.fix_pricing_instance = FixPricing(fix.Session, username, password)

        self.fix_settings = fix.SessionSettings(self.config_file)
        self.fix_store_factory = fix.FileStoreFactory(self.fix_settings)
        self.log_factory = fix.ScreenLogFactory(self.fix_settings)

        self.initiator = fix.SocketInitiator(self.fix_pricing_instance,
                                             self.fix_store_factory,
                                             self.fix_settings,
                                             self.log_factory)

        self.initiator.start()