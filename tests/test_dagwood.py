import unittest
import logging
import os
import tempfile
from dagwood import assemble

class TestDagwoodAssemble(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def test_assemble_basic(self):
        # Test basic functionality
        logger = assemble(folder_name=self.temp_dir)
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.level, logging.INFO)

    def test_assemble_folder_creation(self):
        # Test if log folder is created
        assemble(folder_name=self.temp_dir)
        self.assertTrue(os.path.exists(self.temp_dir))

    def test_assemble_file_creation(self):
        # Test if log file is created
        assemble(folder_name=self.temp_dir)
        self.assertTrue(any(fname.endswith('.log') for fname in os.listdir(self.temp_dir)))

    def test_assemble_custom_level(self):
        # Test custom log level
        logger = assemble(folder_name=self.temp_dir, level=logging.DEBUG)
        self.assertEqual(logger.level, logging.DEBUG)

    def test_assemble_custom_format(self):
        # Test custom log format
        custom_format = '%(levelname)s - %(message)s'
        logger = assemble(folder_name=self.temp_dir, format=custom_format)
        file_handler = logger.handlers[-1]  # Assuming the file handler is the last one
        self.assertEqual(file_handler.formatter._fmt, custom_format)

    def test_assemble_custom_file_name(self):
        # Test custom file name
        custom_file_name = 'custom.log'
        assemble(folder_name=self.temp_dir, file_name=custom_file_name)
        self.assertTrue(custom_file_name in os.listdir(self.temp_dir))

if __name__ == '__main__':
    unittest.main()
