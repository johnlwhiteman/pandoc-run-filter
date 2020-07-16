import os
import shutil
from unittest import TestCase
import pandoc_run_filter as prf

DIR     = os.path.dirname(os.path.realpath(__file__))
FLAGS   = '--from=markdown --standalone --self-contained'
FILTERS = '--filter pandoc-run-filter'
ODIR    = './__pandoc_run__'
ARGS    = f'''{FLAGS} {FILTERS} --to epub3 --metadata title=Test -o {ODIR}/'''

class Tests(TestCase):

    def rm_file(self, path):
        if os.path.isfile(path):
            os.unlink(path)

    def rm_dir(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path)

    '''Verify pandoc-run-filter is in path'''
    def test_001(self):
         self.assertIsNotNone(shutil.which('pandoc-run-filter'))

    '''Verify pandoc is in path'''
    def test_002(self):
         self.assertIsNotNone(shutil.which('pandoc'))

    '''Verify artifacts directory gets created'''
    def test_003(self):
        self.rm_dir(prf.ARTIFACTS_DIR)
        prf.initialize()
        rc = os.path.isdir(prf.ARTIFACTS_DIR)
        self.rm_dir(prf.ARTIFACTS_DIR)
        self.assertTrue(rc)

    '''Verify debug file is created'''
    def test_004(self):
        self.rm_dir(prf.ARTIFACTS_DIR)
        prf.initialize()
        prf.debug('Some debug message.')
        rc = os.path.isfile(prf.DEBUG_FILE)
        if rc == True:
            with open(prf.DEBUG_FILE) as fd:
                content = fd.read().strip()
                rc = content == 'Some debug message.'
            self.rm_dir(prf.ARTIFACTS_DIR)
        self.assertTrue(rc)

    '''Verify in="shell" out="text"'''
    def test_01(self):
        t = '01'
        cmd = f'''pandoc -i {t}.md {ARGS}/{t}.epub'''
        path = f'''{prf.ARTIFACTS_DIR}/{t}.epub'''
        os.chdir(DIR)
        if os.path.isfile(path):
            os.unlink(path)
        rc = os.system(cmd)
        if 0 == rc:
            rc = os.path.isfile(path)
        else:
            rc = False
        self.assertTrue(rc)

    '''Verify in="shell" out="image"'''
    def test_02(self):
        t = '02'
        cmd = f'''pandoc -i {t}.md {ARGS}/{t}.epub'''
        path = f'''{prf.ARTIFACTS_DIR}/{t}.epub'''
        os.chdir(DIR)
        if os.path.isfile(path):
            os.unlink(path)
        rc = os.system(cmd)
        if 0 == rc:
            rc = os.path.isfile(path)
        else:
            rc = False
        self.assertTrue(rc)

    '''Verify in="script" out="text"'''
    def test_03(self):
        t = '03'
        cmd = f'''pandoc -i {t}.md {ARGS}/{t}.epub'''
        path = f'''{prf.ARTIFACTS_DIR}/{t}.epub'''
        os.chdir(DIR)
        if os.path.isfile(path):
            os.unlink(path)
        rc = os.system(cmd)
        if 0 == rc:
            rc = os.path.isfile(path)
        else:
            rc = False
        self.assertTrue(rc)

    '''Verify in="script" out="image img="04.png"'''
    def test_04(self):
        t = '04'
        cmd = f'''pandoc -i {t}.md {ARGS}/{t}.epub'''
        path = f'''{prf.ARTIFACTS_DIR}/{t}.epub'''
        os.chdir(DIR)
        if os.path.isfile(path):
            os.unlink(path)
        rc = os.system(cmd)
        if 0 == rc:
            rc = os.path.isfile(path)
        else:
            rc = False
        self.assertTrue(rc)

