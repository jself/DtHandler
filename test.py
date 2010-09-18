from nose.tools import *

def test_dt():
    from django.conf import settings
    from dthandler import DtHandler
    dt = datetime.datetime(2010, 1, 1, 4, 5, 3)
    tz = pytz.timezone(settings.TIME_ZONE)
    dt_local = dt.replace(tzinfo=tz)
    dth = DtHandler(dt)
    assert_equals(dth.localtime.tzinfo, tz)
    assert_equals(dth.localtime.hour, dt.hour)
    assert_equals(dth.localtime.hour, dt_local.hour)

    assert_equals(dth.utc.hour, dt_local.astimezone(pytz.utc).hour)
    assert_equals(dth.utc.tzinfo, pytz.utc)

