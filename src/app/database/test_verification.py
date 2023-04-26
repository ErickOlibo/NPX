import unittest
import sqlite3
#from verification import Verification


class TestVerification(unittest.TestCase):

    def setUp(self):
        # Create a test database and add a user
        self.conn = sqlite3.connect("user.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE testtable (username TEXT, password TEXT)")
        self.cursor.execute("INSERT OR IGNORE INTO testtable VALUES (?, ?)", ("testuser", "testpassword"))
        self.conn.commit()

        # Create a Verification instance to test
        # self.verifier = Verification()

    def tearDown(self):
        self.conn.close()

    # def test_verify_user_valid(self):
    #     # Test that a valid user can be verified
    #     result = self.verifier.verify_user("testuser", "testpassword")
    #     self.assertTrue(result)

    # def test_verify_user_invalid(self):
    #     # Test that an invalid user cannot be verified
    #     result = self.verifier.verify_user("testuser", "wrongpassword")
    #     self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
