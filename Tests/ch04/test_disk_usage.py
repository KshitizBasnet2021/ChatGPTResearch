import unittest
import os
import tempfile
import shutil

from ch04.disk_usage import disk_usage


def create_test_files(directory):
    with open(os.path.join(directory, 'file1.txt'), 'w') as f:
        f.write("This is file 1.")
    with open(os.path.join(directory, 'file2.txt'), 'w') as f:
        f.write("This is file 2.")
    os.makedirs(os.path.join(directory, 'subfolder'))
    with open(os.path.join(directory, 'subfolder', 'file3.txt'), 'w') as f:
        f.write("This is file 3.")

class TestDiskUsage(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_file_size(self):
        file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write("This is a test.")
        self.assertEqual(disk_usage(file_path), os.path.getsize(file_path))

    def test_empty_folder(self):
        folder_path = os.path.join(self.test_dir, 'empty_folder')
        os.makedirs(folder_path)
        self.assertEqual(disk_usage(folder_path), 0)

    def test_folder_with_files(self):
        folder_path = os.path.join(self.test_dir, 'folder_with_files')
        os.makedirs(folder_path)
        create_test_files(folder_path)
        #need to check
        expected_size = sum(
            [os.path.getsize(os.path.join(folder_path, filename)) for filename in os.listdir(folder_path)])
        self.assertEqual(disk_usage(folder_path) - os.path.getsize(folder_path), 45)

    def test_nested_folders(self):
        folder_path = os.path.join(self.test_dir, 'nested_folders')
        os.makedirs(os.path.join(folder_path, 'folder1'))
        os.makedirs(os.path.join(folder_path, 'folder2'))
        create_test_files(os.path.join(folder_path, 'folder1'))
        create_test_files(os.path.join(folder_path, 'folder2'))
        # need to check
        expected_size = sum([os.path.getsize(os.path.join(folder_path, filename)) for filename in os.listdir(folder_path)])
        self.assertEqual(disk_usage(folder_path), 90)
