import logging
log = logging.getLogger('zen.PagerDuty')

from zope.component import adapts
from zope.interface import implements

from Products.ZenModel.actions import IActionBase
from Products.ZenModel.interfaces import IAction
from Products.ZenModel.NotificationSubscription import NotificationSubscription

from Products.ZenUtils.guid.guid import GUIDManager

from Products.Zuul.form import schema
from Products.Zuul.infos import InfoBase
from Products.Zuul.infos.actions import ActionFieldProperty
from Products.Zuul.interfaces import IInfo
from Products.Zuul.utils import ZuulMessageFactory as _t


class IPagerDutyContentInfo(IInfo):
    service_key = schema.TextLine(title=_t(u'Service Key'))
    summary = schema.TextLine(title=_t(u'Summary'))
    description = schema.TextLine(title=_t(u'Description'))

    incident_key = schema.TextLine(
        title=_t(u'Incident Key'),
        group="Advanced")

    details = schema.List(
        title=_t(u'Details'),
        group="Details",
        xtype='cluther-actions-pagerduty-details-field')


class PagerDutyContentInfo(InfoBase):
    implements(IPagerDutyContentInfo)
    adapts(NotificationSubscription)

    service_key = ActionFieldProperty(
        IPagerDutyContentInfo, 'service_key')

    summary = ActionFieldProperty(
        IPagerDutyContentInfo, 'summary')

    description = ActionFieldProperty(
        IPagerDutyContentInfo, 'description')

    incident_key = ActionFieldProperty(
        IPagerDutyContentInfo, 'incident_key')

    details = ActionFieldProperty(
        IPagerDutyContentInfo, 'details')


class PagerDuty(IActionBase):
    implements(IAction)

    id = 'PagerDuty'
    name = 'PagerDuty'

    actionContentInfo = IPagerDutyContentInfo

    def setupAction(self, dmd):
        self.guidManager = GUIDManager(dmd)

    def updateContent(self, content=None, data=None):
        content.update(data)

    def execute(self, notification, signal):
        log.debug("!!! PagerDuty !!!")
