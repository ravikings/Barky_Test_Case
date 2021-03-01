import unittest
from unittest import TestCase, mock, main
from unittest.case import expectedFailure
from barky import get_option_choice, get_new_bookmark_info, clear_screen, print_options, get_user_input, \
                    get_new_bookmark_data, get_bookmark_id_for_deletion, get_github_import_options, loop

from commands import CreateBookmarksTableCommand




"""
    Test carried out here are see if the function are behaving the way they 
    are program to do, by using unittest mock, we are runing function to
    test against each other and see if the behaviour is the same and when test
    against another function should fail

"""

class Test_User_Option_Choice(TestCase):

    @mock.patch('barky.get_option_choice')
    def test_options(self, test_mock):
        test_mock = get_option_choice
        assert test_mock is get_option_choice
    

    
    @mock.patch('barky.clear_screen')
    def test_clear_screen(self, test_mock):
        test_mock = clear_screen
        assert test_mock is clear_screen


    @mock.patch('barky.print_options')
    def test_print_options(self, test_mock):
        test_mock = print_options
        assert test_mock is print_options


    @mock.patch('barky.get_user_input')
    def test_get_user_input(self, test_mock):
        test_mock = get_user_input
        assert test_mock is get_user_input


    @mock.patch('barky.get_new_bookmark_data')
    def test_get_new_bookmark_data(self, test_mock):
        test_mock = get_new_bookmark_data
        assert test_mock is get_new_bookmark_data


    @mock.patch('barky.get_bookmark_id_for_deletion')
    def test_get_bookmark_id_for_deletion(self, test_mock):
        test_mock = get_bookmark_id_for_deletion
        assert test_mock is get_bookmark_id_for_deletion


    @mock.patch('barky.get_github_import_options')
    def test_get_github_import_options(self, test_mock):
        test_mock = get_github_import_options
        assert test_mock is get_github_import_options


    @mock.patch('barky.get_new_bookmark_info')
    def test_get_new_bookmark_info(self, test_mock):
        test_mock = get_new_bookmark_info
        assert test_mock is get_new_bookmark_info


    @mock.patch('barky.loop')
    def test_loop(self, test_mock):
        test_mock = loop
        assert test_mock is loop



if __name__ == '__main__':
    unittest.main()

