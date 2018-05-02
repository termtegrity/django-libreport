from mock import patch
from datetime import datetime
from django.test import TestCase

from reports.models import ReportSchedule
from reports.runtests.example.models import Organization


class ScheduleReportModelTestCase(TestCase):

    @patch('django.utils.timezone.now')
    def test_datetimes_by_period(self, mNow):

        mNow.return_value = datetime(2012, 12, 12, 12, 12, 12)
        org = Organization(name='Org')

        # Daily
        daily = ReportSchedule(organization=org)
        daily.period = ReportSchedule.PERIOD_DAILY
        start, end = daily.datetimes_by_period()
        self.assertEquals(start, datetime(2012, 12, 11, 0, 0, 0))
        self.assertEquals(end, datetime(2012, 12, 11, 23, 59, 59))

        # Weekly
        weekly = ReportSchedule(organization=org)
        weekly.period = ReportSchedule.PERIOD_WEEKLY
        start, end = weekly.datetimes_by_period()
        self.assertEquals(start, datetime(2012, 12, 3, 0, 0, 0))
        self.assertEquals(end, datetime(2012, 12, 9, 23, 59, 59))

        # Monthly
        monthly = ReportSchedule(organization=org)
        monthly.period = ReportSchedule.PERIOD_MONTHLY
        start, end = monthly.datetimes_by_period()
        self.assertEquals(start, datetime(2012, 11, 1, 0, 0, 0))
        self.assertEquals(end, datetime(2012, 11, 30, 23, 59, 59))

        # Yearly
        yearly = ReportSchedule(organization=org)
        yearly.period = ReportSchedule.PERIOD_YEARLY
        start, end = yearly.datetimes_by_period()
        self.assertEquals(start, datetime(2011, 1, 1, 0, 0, 0))
        self.assertEquals(end, datetime(2011, 12, 31, 23, 59, 59))
