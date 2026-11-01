"""Automated tests for the Phishing URL Awareness Checker."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phishing_checker import check_url


class PhishingCheckerTests(unittest.TestCase):
    def test_example_url_no_listed_signs(self):
        self.assertEqual(check_url("https://www.example.com/login"), [])

    def test_ip_address_and_http(self):
        result = check_url("http://192.0.2.10/account")
        self.assertTrue(any("IP address" in x for x in result))
        self.assertTrue(any("HTTP" in x for x in result))

    def test_at_symbol_and_http(self):
        result = check_url("http://example.com@sample.invalid/login")
        self.assertTrue(any("@' symbol" in x for x in result))
        self.assertTrue(any("HTTP" in x for x in result))

    def test_many_hostname_segments(self):
        result = check_url("https://a.b.c.d.e.example.invalid/path")
        self.assertTrue(any("5 or more" in x for x in result))

    def test_punycode_marker(self):
        result = check_url("https://xn--example.invalid/")
        self.assertTrue(any("punycode" in x for x in result))

    def test_blank_input(self):
        with self.assertRaises(ValueError):
            check_url("")


if __name__ == "__main__":
    unittest.main()
