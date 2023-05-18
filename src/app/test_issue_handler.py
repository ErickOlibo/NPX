"""This module tests IssueHandler using unittest."""
import unittest
from issue_handler import IssueHandler
from helpers import SessionData, IssueMessage, StartUp

class TestIssueHandler(unittest.TestCase):
    
    def setUp(self) -> None:
        self.handler = IssueHandler()
    
    def tearDown(self):
        pass
    
    def test_issue_handler(self):
        data = SessionData("", "12345", StartUp.LOG_IN)
        resp = self.handler.get_issue_message(data)
        self.assertEqual(resp, IssueMessage.EMPTY_USERNAME)
        data = SessionData("Erick", "", StartUp.LOG_IN)
        resp = self.handler.get_issue_message(data)
        self.assertEqual(resp, IssueMessage.EMPTY_PASSWORD)
    
    def test_issue_message(self):
        data = SessionData("Erick", "12345", StartUp.LOG_IN)
        issue = self.handler.get_issue_message(data)
        self.assertIsInstance(issue, IssueMessage)
        
        data = SessionData("Erick", "12345", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertIsInstance(issue, IssueMessage)
        
        data = SessionData("Erick", "12345", "")
        issue = self.handler.get_issue_message(data)
        self.assertIsInstance(issue, IssueMessage)
    
    def test_sign_in_issue(self):
        data = SessionData("Er", "12345", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.SHORT_USERNAME)
        
        data = SessionData("This is a long user name", "12345", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.LONG_USERNAME)
        
        data = SessionData("Tester_One", "12345", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.MISSING_SPECIAL)
        
        data = SessionData("Tester_One", "!123", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.NO_LOWER_PASSWORD)
        
        data = SessionData("Tester_One", "!13aa", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.NO_UPPER_PASSWORD)
        
        data = SessionData("Tester_One", "!aaA", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.WEAK_PASSWORD)
        
        data = SessionData("Tester_One", "!aa!AA!aa", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.NO_DIGIT_PASSWORD)
        
        data = SessionData("Erick", "!aa!AA!aa", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.USERNAME_TAKEN)

    def test_log_in_issue(self):
        data = SessionData("Tester_Two", "!13aa", StartUp.SIGN_IN)
        issue = self.handler.get_issue_message(data)
        self.assertEqual(issue, IssueMessage.NO_UPPER_PASSWORD)
    


if __name__ == '__main__':
    unittest.main()
