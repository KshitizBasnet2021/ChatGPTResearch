import unittest
import tempfile
import os

from ch04.No_Comments.disk_usage import disk_usage


class TestDiskUsage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_test_structure(self):
        # Create a temporary directory with nested files and directories
        test_dir = os.path.join(self.temp_dir.name, 'test_dir')
        os.makedirs(test_dir)

        file1_path = os.path.join(test_dir, 'file1.txt')
        with open(file1_path, 'w') as f:
            f.write('This is file 1.')

        sub_dir_path = os.path.join(test_dir, 'sub_dir')
        os.makedirs(sub_dir_path)

        file2_path = os.path.join(sub_dir_path, 'file2.txt')
        with open(file2_path, 'w') as f:
            f.write('This is file 2.')

    def test_empty_directory(self):
        path = self.temp_dir.name
        result = disk_usage(path)
        self.assertEqual(result, 0)

    def test_file_only(self):
        file_path = os.path.join(self.temp_dir.name, 'file.txt')
        with open(file_path, 'w') as f:
            f.write('This is a test file.')

        result = disk_usage(file_path)
        self.assertEqual(result, os.path.getsize(file_path))

    def test_directory_with_files(self):
        self.create_test_structure()
        path = os.path.join(self.temp_dir.name, 'test_dir')
        expected_total = (
                os.path.getsize(os.path.join(path, 'file1.txt')) +
                os.path.getsize(os.path.join(path, 'sub_dir', 'file2.txt'))
        )
        result = disk_usage(path)
        self.assertEqual(result, expected_total)

