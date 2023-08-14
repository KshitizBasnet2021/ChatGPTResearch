import unittest
import os
from unittest.mock import patch

from ch04.disk_usage import disk_usage


class TestDiskUsage(unittest.TestCase):

    def test_file_size(self):
        with open('test_file.txt', 'w') as f:
            f.write("This is a test.")
        path = 'test_file.txt'
        self.assertEqual(disk_usage(path), os.path.getsize(path))
        os.remove(path)

    def test_empty_folder(self):
        path = 'empty_folder'
        os.makedirs(path)
        self.assertEqual(disk_usage(path), 0)
        os.rmdir(path)

    def test_folder_with_files(self):
        path = 'folder_with_files'
        os.makedirs(path)
        with open(os.path.join(path, 'file1.txt'), 'w') as f:
            f.write("This is file 1.")
        with open(os.path.join(path, 'file2.txt'), 'w') as f:
            f.write("This is file 2.")
        expected_size = sum([os.path.getsize(os.path.join(path, filename)) for filename in os.listdir(path)])
        self.assertEqual(disk_usage(path), expected_size)
        for filename in os.listdir(path):
            os.remove(os.path.join(path, filename))
        os.rmdir(path)

    def test_nested_folders(self):
        path = 'nested_folders'
        os.makedirs(os.path.join(path, 'folder1'))
        os.makedirs(os.path.join(path, 'folder2'))
        with open(os.path.join(path, 'folder1', 'file1.txt'), 'w') as f:
            f.write("This is file 1.")
        with open(os.path.join(path, 'folder2', 'file2.txt'), 'w') as f:
            f.write("This is file 2.")
        expected_size = sum([os.path.getsize(os.path.join(path, filename)) for filename in os.listdir(path)])
        self.assertEqual(disk_usage(path), expected_size)
        for filename in os.listdir(path):
            os.remove(os.path.join(path, filename))
        os.rmdir(os.path.join(path, 'folder1'))
        os.rmdir(os.path.join(path, 'folder2'))
        os.rmdir(path)

    @patch("os.path.getsize")
    def test_mocked_os_getsize(self, mock_getsize):
        mock_getsize.return_value = 100
        path = 'mocked_file.txt'
        self.assertEqual(disk_usage(path), 100)

if __name__ == '__main__':
    unittest.main()
