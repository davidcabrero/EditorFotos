#!/usr/bin/python3
import filecmp
import sys
import unittest

import transform_args

class TestMirrorGrayscale(unittest.TestCase):

    def test_simple(self):

        sys.argv = ['program.py', '../cafe.jpg', 'mirror', 'grayscale']
        transform_args.main()
        self.assertTrue(filecmp.cmp('cafe_mirror_gray.jpg', '../cafe_trans.jpg'),
                        msg="Files are different")

if __name__ == '__main__':
    unittest.main()
