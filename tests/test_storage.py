#!/usr/share/env python3

import tempfile
import pytest

from src.pgbackup import storage

@pytest.fixture
def in_file():
    file = tempfile.TemporaryFile()
    file.write(b'Testing')
    file.seek(0)
    return file

def test_storing_file_locally(in_file):
    """
    Writes content from one file-like to another
    """

    #pg dump is in bytes so we shloud test files in bytes mode - so default option in tempfile
    out_file = tempfile.NamedTemporaryFile(delete=False)
    storage.local(in_file, out_file)

    with open(out_file.name, 'rb') as file:
        assert file.read() == b'Testing'

def tests_storing_file_on_s3(mocker, in_file):
    """
    Write content from one file to S3
    """
    client = mocker.Mock()

    storage.s3(client, in_file, "bucket", "file-name")

    client.upload_fileobj.assert_called_with(infile, "bucket", "file-name")