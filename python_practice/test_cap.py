import unittest
import cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		print('hello')
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Python')

if __name__ == '__main__':
	testcap = TestCap();
	testcap.test_one_word()