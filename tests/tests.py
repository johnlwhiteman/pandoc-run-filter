import os
import shutil
from unittest import TestCase
import pandoc_run_filter as prf

DIR = os.path.dirname(os.path.realpath(__file__))

class Tests(TestCase):

    def rm_file(self, path):
        if os.path.isfile(path):
            os.unlink(path)

    def rm_dir(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path)

    '''Verify pandoc-run-filter is in path'''
    def test_01(self):
         self.assertIsNotNone(shutil.which('pandoc-run-filter'))

    '''Verify pandoc is in path'''
    def test_02(self):
         self.assertIsNotNone(shutil.which('pandoc'))

    '''Verify artifacts directory gets created'''
    def test_03(self):
        self.rm_dir(prf.ARTIFACTS_DIR)
        prf.initialize()
        rc = os.path.isdir(prf.ARTIFACTS_DIR)
        self.rm_dir(prf.ARTIFACTS_DIR)
        self.assertTrue(rc)

    '''Verify debug file is created'''
    def test_04(self):
        self.rm_dir(prf.ARTIFACTS_DIR)
        prf.initialize()
        prf.debug('Hello Squirrel')
        rc = os.path.isfile(prf.DEBUG_FILE)
        if rc == True:
            with open(prf.DEBUG_FILE) as fd:
                content = fd.read().strip()
                rc = content == 'Hello Squirrel'
            self.rm_dir(prf.ARTIFACTS_DIR)
        self.assertTrue(rc)

    '''Verify in="shell" out="text"'''
    def test_05(self):
        path = '01.epub'
        os.chdir(DIR)
        if os.path.isfile(path):
            os.unlink(path)
        rc = os.system('make 01')
        if 0 == rc:
            rc = os.path.isfile(path)
        else:
            rc = False
        self.assertTrue(rc)

    '''Verify in="shell" out="image"'''
    def test_06(self):
        path = '02.epub'
        os.chdir(DIR)
        if os.path.isfile(path):
            os.unlink(path)
        rc = os.system('make 02')
        if 0 == rc:
            rc = os.path.isfile(path)
        else:
            rc = False
        self.assertTrue(rc)