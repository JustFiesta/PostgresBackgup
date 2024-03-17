#!/usr/share/env python3

def local(in_file, out_file):
    out_file.write(in_file.read())
    out_file.close()
    in_file.close()

def s3(client, in_file, bucket, filename):
    client.upload_fileobj(in_file, bucket, filename)
