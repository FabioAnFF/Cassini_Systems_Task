import unittest
from helpers.helpers import *

credentials_file = 'resources/Credentials.xlsx'
crendetials_sheet = 'Credentials'

reqres_auth_file = 'resources/reqres_logins.json'


class TestReqresAPI(unittest.TestCase):
    reqres_url = 'https://reqres.in/api'
    reqres_register_path = "register"
    reqres_login_path = "login"
    reqres_resource_path = "resources"

    # •	REGISTER - SUCCESSFUL
    def test_successful_register(self):
        register_params = get_json_values_by_key(reqres_auth_file, "register_params")

        response = issue_request(
            method="POST",
            url=self.reqres_url,
            path=self.reqres_register_path,
            data=register_params
        )

        self.assertEqual(response.status_code, requests.codes.ok,
                         "Response status code did not return expected good response.")
        self.assertIn("token", response.json(), "Token not found in response.")

    # •	LOGIN - SUCCESSFUL
    def test_successful_login(self):
        login_params = get_json_values_by_key(reqres_auth_file, "login_params")
        response = issue_request(
            method="POST",
            url=self.reqres_url,
            path=self.reqres_login_path,
            data=login_params
        )

        self.assertEqual(response.status_code, requests.codes.ok,
                         "Response status code did not return expected bad response.")
        self.assertIn("token", response.json(), "Token not found in response.")

    # •	LIST <RESOURCE> - Implement assertion for one of the id and resource
    def test_list_resource(self):
        response = issue_request(
            method="GET",
            url=self.reqres_url,
            path=self.reqres_resource_path
        )

        self.assertEqual(response.status_code, requests.codes.ok,
                         "Response status code did not return expected good response.")

        first_resource = response.json()['data'][0]

        self.assertEqual(first_resource['id'], 1, "First resource does not have an ID of 1.")
        self.assertEqual(first_resource['year'], 2000, "First resource does not have a year of 2000.")


# Also, implement a scenario to read data from Excel or JSON.

class TestFileReaders(unittest.TestCase):

    def test_read_from_xls(self):
        file_rows = read_xls_file(credentials_file, crendetials_sheet)
        first_row = file_rows[0]
        self.assertEqual(first_row[0], "FirstTestLogin_12", "First username is not FirstTestLogin_12")
        self.assertEqual(first_row[1], "TestAbc_12!", "First password is not TestAbc_12!")
