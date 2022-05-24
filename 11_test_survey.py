import unittest
Survey  = __import__('11_survey')

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored correctly."""
        question = 'What language did you first learn to speak?'
        my_survey = Survey.AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)

    def test_store_three_response(self):
        """Test that three individual responses are stored correctly."""
        question = 'What language did you first learn to speak?'
        my_survey = Survey.AnonymousSurvey(question)
        responses = ['English','French','Italian']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)

if __name__ == '__main__':
    unittest.main()