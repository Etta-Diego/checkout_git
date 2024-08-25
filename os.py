#!/usr/bin/python3
import os

dirname = '~/alx-system_engineering-devops'
for basename in os.listdir(dirname):
  path = os.path.join(dirname, basename)
  if os.path.isdir(path):
    print('folder: {0}'.format(path))
  else:
    print('file:   {0}'.format(path))
