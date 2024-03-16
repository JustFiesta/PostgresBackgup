import pytest
from src.pgbackup import cli

#$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

url = "postgres://bob@example.com:5432/db_one"

# function returning function - enables developers to inject function to other functions
@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    #doc string
    """
    Without a specified driver - parser will exit
    """

    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):
    """
    The parser will exit if it recives a driver without a destination
    """

    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_unknown_driver(parser):
    """"
    The parser will exit if driver is uknown
    """

    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", 'destination'])

def test_parser_with_known_driver(parser):
    """"
    The parser will NOT exit if driver is uknown
    """

    for driver in ['local', 's3']:
        assert parser.parse_args([url, "--driver", driver, 'destination'])

    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", 'destination'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it recives a driver and destination
    """

    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/path'