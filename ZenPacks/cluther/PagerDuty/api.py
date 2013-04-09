import logging
log = logging.getLogger('zen.PagerDuty')

from Products.ZenUtils.Ext import DirectRouter, DirectResponse


class PagerDutyRouter(DirectRouter):
    def loadSettings(self, load=True):
        dmd = self.context

        log.info("Returning PagerDuty settings")
        return DirectResponse(data={
            'api_access_key': dmd.pagerduty_api_access_key,
            })

    def submitSettings(self, api_access_key=None):
        dmd = self.context

        log.info("Setting API access key to %s", api_access_key)
        dmd.pagerduty_api_access_key = api_access_key
