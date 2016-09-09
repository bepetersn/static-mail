import contextlib
from functools import partial
from .base import MailWrapper


def patch_argument(cb, kname, default=None, **kwargs):
    return cb(kwargs.get(kname, default))


def patch_arguments(cb, kname, default=None, **kwargs):
    kwargs[kname] = patch_argument(cb, kname, default, **kwargs)
    return kwargs


class YAGMailWrapper(MailWrapper):

    def __init__(self, config):
        super(YAGMailWrapper, self).__init__(config)

        # templated_mail shouldn't open a connection
        # until it's required, but yagmail does upon
        # instantiation, so we have to manage
        # it closely to get around that.
        self._yag_config = self._prepare_config()
        self._smtp_cls = self._choose_smtp_cls()
        self._smtp = partial(self._smtp_cls, **self._yag_config)

        # These will help us send multiple emails
        # in an STMP session if we so desire.
        self._connection = None
        self._keep_connected = False

    def _choose_smtp_cls(self):
        # Don't require yagmail be installed
        # to use templated_mail.
        from yagmail import yagmail
        # Use the correct class depending on whether
        # it looks like TLS is being used; if not,
        # assume use of SSL & port 465
        return (yagmail.SMTP if int(self._yag_config['port']) == 587
                else yagmail.SMTP_SSL)

    def _prepare_config(self):

        # Create the kind of config yagmail expects
        # from the config that templated-mail supports
        return {
            'host': self.config.MAIL_HOST,
            'port': self.config.MAIL_PORT,
            'user': {self.config.EMAIL_ADDRESS: self.config.NAME},
            'password': self.config.EMAIL_PASSWORD,
            'smtp_set_debuglevel': self.config.DEBUG
        }

    def _extra_headers(self, **kwargs):
        return {
            'Reply-To': patch_argument(
                lambda r: r if r is not None else self.config.REPLY_TO,
                'reply_to', **kwargs
            )
        }

    @contextlib.contextmanager
    def connect(self):
        self._keep_connected = True
        try:
            with self._stmp() as conn:
                self._connection = conn
                yield
        finally:
            self._connection = None
            self._keep_connected = False

    def send_message(self, rendered, *args, **kwargs):

        # Login if this is a one-off message
        if self._connection is None:
            self._connection = self._smtp()
        else:
            if self._connection.is_closed:
                self._connection.login(self.config.EMAIL_PASSWORD)

        kwargs = patch_arguments(
            lambda h: h.update(self._extra_headers(**kwargs)),
            'headers', default={}, **kwargs
        )
        kwargs = patch_arguments(
            lambda p: p if p is not None else self.config.SUPPRESS,
            'preview_only', **kwargs
        )

        self._connection.send(
            subject=rendered.subject,
            contents=[rendered.html.strip()],
            **kwargs
        )

        # Logout if this is a one-off message
        if not self._keep_connected:
            self._connection.close()


Mail = YAGMailWrapper