import sys
import subprocess

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: pg_dump not found\n{err}")
        sys.exit(2)

def dump_file_name(url, timestamp):
    db_name = url.split("/")[-1] # get last element after the / - with happens to often be the db name

    db_name = db_name.split("?")[0] #dont include query in url address

    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"