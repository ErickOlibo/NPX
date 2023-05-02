import re


class IssueHandler:
    """TO_FILL_IN_LATER."""

   
        """__init___."""
       
 def _password_requirements(self, data: SessionData) -> IssueMessage:
        if not re.search(r"[!@#$%^&*?]", data.password):
            return IssueMessage.MISSING_SPECIAL
        if not re.search(r"[a-z]", data.password):
            return IssueMessage.NO_LOWER_PASSWORD
        if not re.search(r"[A-Z]", data.password):
            return IssueMessage.NO_UPPER_PASSWORD
        if len(data.password) < 8:
            return IssueMessage.WEAK_PASSWORD
        if not re.search(r"\d", data.password):
            return IssueMessage.NO_DIGIT_PASSWORD
        return IssueMessage.NONE
