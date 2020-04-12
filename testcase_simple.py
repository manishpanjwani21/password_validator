#!/usr/bin/env python

import unittest
from password_validator import password_check

class PasswordTestCase(unittest.TestCase):
    """Tests for `password_validator`."""
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        with open('weak_password_list.txt') as filetext:
            self.filedata = filetext.read()
    """Tests for `password_validator`."""
    
    def test_is_non_ascii_character(self):
        """Is password check for non_ascii_character ?"""
        self.assertFalse(password_check('hello aåbäcö',self.filedata))
    
    def test_is_short_character(self):
        """Is password check for short_character ?"""
        self.assertFalse(password_check('mom',self.filedata))
    
    def test_is_long_character(self):
        """Is password check for long_character?"""
        self.assertFalse(password_check('aaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssssssssdddddddssasadsssss',self.filedata))
    
    def test_is_common_password(self):
        """Is password check for common_password?"""
        self.assertFalse(password_check('password1',self.filedata))

if __name__ == '__main__':
    unittest.main()
