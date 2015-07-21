# -*- coding: utf-8 -*-
"""Tests for the `subler.utils` functions"""
import subprocess
import unittest

from mock import patch

from subler.utils import subler_executable, get_output

check_output = 'subler.utils.subprocess.check_output'


class ExecutableTests(unittest.TestCase):
    """Tests for the subler_executable function"""

    def test_shell_success(self):
        """Verify that when we get a valid response that that is propogated as
        expected
        """
        out = b'/usr/bin/SublerCLI'
        with patch(check_output, return_value=out):
            self.assertEqual(subler_executable(), out.decode('UTF-8'))

    def test_empty_string(self):
        """Test that an empty string result is handled as expected"""
        with patch(check_output, return_value=b''):
            self.assertEqual(subler_executable(), 'SublerCLI')

    def test_shell_error(self):
        """Test that subprocess.CalledProcessErrors are handled gracefully"""
        with patch(check_output,
                   side_effect=subprocess.CalledProcessError(1, '')):
            self.assertEqual(subler_executable(), '')


class GetOutputTests(unittest.TestCase):
    """Tests for the get_output function"""

    def setUp(self):
        self.date_output = b'Mon Jul 20 21:48:58 EDT 2015'
        self.expected = self.date_output.decode('UTF-8').strip()

    def test_list(self):
        """Test that check_output properly handles accepting and passing off a
        provided list of commandline arguments
        """
        args = ['date']
        with patch(check_output, return_value=self.date_output):
            self.assertEqual(get_output(args), self.expected)

    def test_str(self):
        """Test that check_output properly handles accepting and passing off a
        provided string of commandline arguments
        """
        args = 'date'
        with patch(check_output, return_value=self.date_output):
            self.assertEqual(get_output(args), self.expected)
