from django.conf import settings
import pytz

class DtHandler(object):
    def __init__(self, dt):
        self.dt = dt

    @property
    def localzone(self):
        if hasattr(self, '_localzone'):
            return self._localzone
        tz = pytz.timezone(settings.TIME_ZONE)
        self._localzone = tz
        return tz

    @property
    def localtime(self, dt=None):
        dt = dt or self.dt
        if dt.tzinfo and dt.tzinfo != self.localzone:
            return dt.astimezone(self.localzone)
        self.dt = self.dt.replace(tzinfo=self.localzone)
        return self.dt

    @property
    def utc(self):
        return self.localtime.astimezone(pytz.utc)



