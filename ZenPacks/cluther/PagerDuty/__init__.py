import Globals

from Products.ZenModel.ZenossSecurity import ZEN_MANAGE_DMD
from Products.ZenModel.DataRoot import DataRoot
from Products.ZenModel.UserSettings import UserSettingsManager
from Products.ZenModel.ZenossInfo import ZenossInfo
from Products.ZenModel.ZenPackManager import ZenPackManager
from Products.ZenUtils.Utils import unused
unused(Globals)


# Add "PagerDuty" to left navigation on Advanced / Settings page. This
# is so ugly because the settings page is still a Zenoss 2 "back-compat"
# page.
for klass in (DataRoot, UserSettingsManager, ZenossInfo, ZenPackManager):
    action = '../dmd/pagerduty'
    if klass == ZenPackManager:
        action = '../%s' % action

    fti = klass.factory_type_information[0]
    fti['actions'] = fti['actions'] + ({
        'id': 'pagerduty',
        'name': 'PagerDuty',
        'action': action,
        'permissions': (ZEN_MANAGE_DMD,)
    },)
