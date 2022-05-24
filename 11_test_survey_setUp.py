from http.client import responses
import unittest
Survey  = __import__('11_survey')

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    # set up method is valauble to store things that are used in multiple test cases
    def setUp(self):
        """Create a survey and set of responses for use in all test methods"""
        question  = "What language did you first learn to speak?"
        self.my_survey = Survey.AnonymousSurvey(question)
        self.responses = ['English','French','Italian']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()