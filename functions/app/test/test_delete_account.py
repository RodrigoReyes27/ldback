import unittest

from .. import create_app


class DeleteAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.headers = {
            "Content-Type": "application/json",
        }

    def tearDown(self):
        self.app_context.pop()

    def test_error_return(self):
        reponse = self.client.post(
            "/user/delete_account", headers=self.headers, json={"sure": "not_sure"}
        )
        self.assertEqual(reponse.status_code, 400)
