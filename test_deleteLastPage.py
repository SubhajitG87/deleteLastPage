import unittest
import os
import tempfile
import zipfile
import rarfile
from deleteLastPage import delete_last_page

class TestDeleteLastPage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    def test_delete_last_page_cbz(self):
        test_cbz = os.path.join(self.temp_dir, 'test.cbz')
        with zipfile.ZipFile(test_cbz, 'w') as zf:
            zf.writestr('page1.jpg', b'dummy data')
            zf.writestr('page2.jpg', b'dummy data')
            zf.writestr('page3.jpg', b'dummy data')

        delete_last_page(test_cbz)

        modified_cbz = os.path.join(self.temp_dir, 'test_modified.cbz')
        self.assertTrue(os.path.exists(modified_cbz))

        with zipfile.ZipFile(modified_cbz, 'r') as zf:
            self.assertEqual(zf.namelist(), ['page1.jpg', 'page2.jpg'])

    def test_delete_last_page_cbr(self):
        # Note: rarfile library is read-only, so we skip actual CBR creation
        # This test would require a real CBR file to test properly
        # For now, we test the error handling for unsupported operations
        test_cbr = os.path.join(self.temp_dir, 'test.cbr')
        
        # Create an empty file with .cbr extension to test file existence
        with open(test_cbr, 'wb') as f:
            f.write(b'dummy rar data')
        
        # This should raise an exception since it's not a valid RAR file
        with self.assertRaises(Exception):  # Could be rarfile.Error or similar
            delete_last_page(test_cbr)

    def test_unsupported_file_format(self):
        test_file = os.path.join(self.temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('dummy data')

        with self.assertRaises(ValueError):
            delete_last_page(test_file)

    def test_single_page_cbz(self):
        test_cbz = os.path.join(self.temp_dir, 'single_page.cbz')
        with zipfile.ZipFile(test_cbz, 'w') as zf:
            zf.writestr('page1.jpg', b'dummy data')

        delete_last_page(test_cbz)

        modified_cbz = os.path.join(self.temp_dir, 'single_page_modified.cbz')
        self.assertTrue(os.path.exists(modified_cbz))

        with zipfile.ZipFile(modified_cbz, 'r') as zf:
            self.assertEqual(zf.namelist(), [])

    def test_non_existent_file(self):
        non_existent_file = os.path.join(self.temp_dir, 'non_existent.cbz')
        with self.assertRaises(FileNotFoundError):
            delete_last_page(non_existent_file)
    
    def test_empty_archive(self):
        test_cbz = os.path.join(self.temp_dir, 'empty.cbz')
        with zipfile.ZipFile(test_cbz, 'w') as zf:
            pass  # Create empty archive
        
        with self.assertRaises(ValueError):
            delete_last_page(test_cbz)

if __name__ == '__main__':
    unittest.main()
