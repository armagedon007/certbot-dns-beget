"""Tests for certbot_dns_beget._internal.dns_beget."""

import unittest


try:
    import mock
except ImportError: # pragma: no cover
    from unittest import mock # type: ignore
from requests.exceptions import HTTPError

from certbot.compat import os
from certbot.plugins import dns_test_common
from certbot.plugins import dns_test_common_lexicon
from certbot.plugins.dns_test_common import DOMAIN
from certbot.tests import util as test_util

LOGIN = 'demo'
PASSWORD = 'demo'
VALID_CONFIG = {"login": LOGIN, "password": PASSWORD}


class AuthenticatorTest(test_util.TempDirTestCase, dns_test_common.BaseAuthenticatorTest):

    def setUp(self):
        from certbot_dns_beget._internal.dns_beget import Authenticator

        super(AuthenticatorTest, self).setUp()

        path = os.path.join(self.tempdir, 'file.ini')
        dns_test_common.write(VALID_CONFIG, path)

        self.config = mock.MagicMock(beget_credentials=path,
                                     beget_propagation_seconds=0)  # don't wait during tests

        self.auth = Authenticator(self.config, "beget")

        self.mock_client = mock.MagicMock()
        # _get_beget_client | pylint: disable=protected-access
        self.auth._get_beget_client = mock.MagicMock(return_value=self.mock_client)


class BegetClientTest(unittest.TestCase):
    DOMAIN_NOT_FOUND = HTTPError('404 Client Error: Not Found for url: {0}.'.format(DOMAIN))
    LOGIN_ERROR = HTTPError('401 Client Error: Unauthorized for url: {0}.'.format(DOMAIN))

    def setUp(self):
        from certbot_dns_beget._internal.dns_beget import _BegetClient
        self.beget_client = _BegetClient(LOGIN, PASSWORD)
       
    def test_find_records(self):

        # _find_domain | pylint: disable=protected-access
        r = ''

if __name__ == "__main__":
    unittest.main()  # pragma: no cover
