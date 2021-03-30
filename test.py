import unittest
import os

from image_pdf_tools import (
    image_to_pdf,
    pdf_merge
)

class TestImagePDFtools(unittest.TestCase):
	def setUp(self):
		self.image_file = os.path.join('examples/results', 'harouna_image.jpg')
		self.pdf_files = [
			os.path.join('examples/results', 'test_pdf_1.pdf'),
			os.path.join('examples/results', 'test_pdf_2.pdf'),
		]
		self.folder_save = 'examples/results'

	def test_image_to_pdf_converter(self):
		result = image_to_pdf('bad_path_file/test.jpg', self.folder_save)
		self.assertFalse(result)
		result = image_to_pdf(self.image_file, 'pad_folder_save/')
		self.assertFalse(result)
		result = image_to_pdf(self.image_file, self.folder_save)
		self.assertTrue(result)

	def test_pdf_merger(self):
		result = pdf_merge(['bad_path_file/test.pdf'], self.folder_save)
		self.assertFalse(result)
		result = pdf_merge(self.pdf_files, 'pad_folder_save/')
		self.assertFalse(result)
		result = pdf_merge(self.pdf_files[0], self.folder_save)
		self.assertFalse(result)
		result = pdf_merge(self.pdf_files, self.folder_save)
		self.assertTrue(result)

	def tearDown(self):
		# add to delete file
		pass
