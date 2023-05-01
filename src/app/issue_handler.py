"""TO_FILL_IN_LATER"""
from helpers import SessionData, IssueMessage, StartUp
from sql_handler import SQLHandler
import re


class IssueHandler:
    """TO_FILL_IN_LATER"""

    def __init__(self):
        self._handler = SQLHandler()

    def get_issue_message(self, data: SessionData) -> IssueMessage:
        """Get the issue type that a session data may have

        parameters
        ----------
            data: SessionData
                Data containing the current session username, password, startup type

        Returns:
            IssueMessage:
                An enum holding the type of issue
        """
        if not data.username or not data.password:
            return self._empty_issue(data)
        if data.type == StartUp.SIGN_IN:
            return self._sign_in_issue(data)
        if data.type == StartUp.LOG_IN:
            return self._log_in_issue(data)
        return IssueMessage.UNKNOWN

    def _empty_issue(self, data: SessionData) -> IssueMessage:
        issue = IssueMessage.NONE
        if not data.username:
            issue = IssueMessage.EMPTY_USERNAME
        if not data.password:
            issue = IssueMessage.EMPTY_PASSWORD
        return issue

    def _sign_in_issue(self, data: SessionData) -> IssueMessage:
        if not self._handler.username_taken(data.username):
            self._handler.insert_into_userdata(data)
            return IssueMessage.NONE
        return IssueMessage.USERNAME_TAKEN

    def _log_in_issue(self, data: SessionData) -> IssueMessage:
        if self._handler.verified_user(data.username, data.password):
            return IssueMessage.NONE
        if self._handler.username_taken(data.username):
            return IssueMessage.WRONG_PASSWORD
        return IssueMessage.WRONG_USERNAME
