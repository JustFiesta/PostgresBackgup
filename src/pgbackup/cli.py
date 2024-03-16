from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']

# extention to Action class, for getting two values for --driver agrument
class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # destruct values into two variables
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Uknown driver. Avalible drivers are: 'local', 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""Back up PostgreSQL databases locally or to AWS S3.""")
    parser.add_argument("url", help="URL of database to backup")
    parser.add_argument("--driver",
        help="how & where to store backup",
        nargs=2,
        action=DriverAction,
        required=True)
    return parser