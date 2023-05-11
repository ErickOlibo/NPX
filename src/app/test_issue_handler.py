"""This module tests IssueHandler using unittest."""
import unittest
from issue_handler import IssueHandler
from helpers import SessionData, IssueMessage, StartUp

class TestIssueHandler(unittest.TestCase):
    
    def setUp(self) -> None:
        self.handler = IssueHandler()
    
    def test_issue_handler(self):
        data = SessionData("", "12345", StartUp.LOG_IN)
        resp = self.handler.get_issue_message(data)
        self.assertEqual(resp, IssueMessage.EMPTY_USERNAME)
        data = SessionData("Erick", "", StartUp.LOG_IN)
        resp = self.handler.get_issue_message(data)
        self.assertEqual(resp, IssueMessage.EMPTY_PASSWORD)


if __name__ == '__main__':
    unittest.main()
