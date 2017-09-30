"""Log and notify admins in case of critical issues."""

class Alter:

    @staticmethod
    def log(self, exception_obj):
        # log it
        if self._need_notify():
            self.notify_admins(message, exception_obj.level)

    @staticmethod
    def _need_notify(self):
        pass

    @staticmethod
    def notify_admins(self, message, level):
        pass