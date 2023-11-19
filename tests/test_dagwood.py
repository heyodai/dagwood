import logging
import os
import tempfile
import pytest
from dagwood import assemble

@pytest.fixture
def temp_dir():
    return tempfile.mkdtemp()

def test_assemble_basic(temp_dir):
    # Test basic functionality
    logger = assemble(folder_name=temp_dir)
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.INFO

def test_assemble_folder_creation(temp_dir):
    # Test if log folder is created
    assemble(folder_name=temp_dir)
    assert os.path.exists(temp_dir)

def test_assemble_file_creation(temp_dir):
    # Test if log file is created
    assemble(folder_name=temp_dir)
    assert any(fname.endswith('.log') for fname in os.listdir(temp_dir))

def test_assemble_custom_level(temp_dir):
    # Test custom log level
    logger = assemble(folder_name=temp_dir, level=logging.DEBUG)
    assert logger.level == logging.DEBUG

def test_assemble_custom_format(temp_dir):
    # Test custom log format
    custom_format = '%(levelname)s - %(message)s'
    logger = assemble(folder_name=temp_dir, format=custom_format)
    file_handler = logger.handlers[-1]  # Assuming the file handler is the last one
    assert file_handler.formatter._fmt == custom_format

def test_assemble_custom_file_name(temp_dir):
    # Test custom file name
    custom_file_name = 'custom.log'
    assemble(folder_name=temp_dir, file_name=custom_file_name)
    assert custom_file_name in os.listdir(temp_dir)
