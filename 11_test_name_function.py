import unittest
# bad import method because I want to keep file names starting with a number.
testing_your_code  = __import__('11_testing_your_code')

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        #run method from imported file
        formatted_name = testing_your_code.get_formatted_name('janis','joplin')
        #compare result of method exuction with expected result
        self.assertEqual(formatted_name,'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like Wolfgang Amadeus Mozart work?"""
        formatted_name = testing_your_code.get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
    