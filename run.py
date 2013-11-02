#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import argparse
import os
import shutil
import sys
import time


################################################################################
# Options
################################################################################
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clean', dest='clean', action='store_true',
    help='''recompiles files when running the development web server, but
    obsolete if -s is used''',
  )
parser.add_argument('-m', '--minify', dest='minify', action='store_true',
    help='compiles files into minified version before deploying'
  )
parser.add_argument('-s', '--start', dest='start', action='store_true',
    help='starts the dev_appserver.py with storage_path pointing to temp',
  )
parser.add_argument('-o', '--host', dest='host', action='store', default='127.0.0.1',
    help='the host to start the dev_appserver.py',
  )
parser.add_argument('-p', '--port', dest='port', action='store', default='8080',
    help='the port to start the dev_appserver.py',
  )
parser.add_argument('-f', '--flush', dest='flush', action='store_true',
    help='clears the datastore, blobstore, etc',
  )
args = parser.parse_args()


################################################################################
# Directories
################################################################################
DIR_MAIN = 'main'
DIR_STATIC = 'static'
DIR_SRC = 'src'
DIR_STYLE = 'style'
DIR_SCRIPT = 'script'
DIR_MIN = 'min'
DIR_DST = 'dst'
DIR_LIB = 'lib'
DIR_NODE_MODULES = 'node_modules'
DIR_BIN = '.bin'
DIR_TEMP = 'temp'
DIR_STORAGE = 'storage'

FILE_ZIP = '%s.zip' % DIR_LIB
FILE_COFFEE = 'coffee'
FILE_LESS = 'lessc'
FILE_UGLIFYJS = 'uglifyjs'

dir_static = os.path.join(DIR_MAIN, DIR_STATIC)

dir_src = os.path.join(dir_static, DIR_SRC)
dir_src_script = os.path.join(dir_src, DIR_SCRIPT)
dir_src_style = os.path.join(dir_src, DIR_STYLE)

dir_dst = os.path.join(dir_static, DIR_DST)
dir_dst_style = os.path.join(dir_dst, DIR_STYLE)
dir_dst_script = os.path.join(dir_dst, DIR_SCRIPT)

dir_min = os.path.join(dir_static, DIR_MIN)
dir_min_style = os.path.join(dir_min, DIR_STYLE)
dir_min_script = os.path.join(dir_min, DIR_SCRIPT)

dir_lib = os.path.join(DIR_MAIN, DIR_LIB)
file_lib = os.path.join(DIR_MAIN, FILE_ZIP)

dir_bin = os.path.join(DIR_NODE_MODULES, DIR_BIN)
file_coffee = os.path.join(dir_bin, FILE_COFFEE)
file_less = os.path.join(dir_bin, FILE_LESS)
file_uglifyjs = os.path.join(dir_bin, FILE_UGLIFYJS)

dir_storage = os.path.join(DIR_TEMP, DIR_STORAGE)


################################################################################
# Helpers
################################################################################
def print_out(script, filename=''):
  timestamp = datetime.now().strftime('%H:%M:%S')
  if not filename:
    filename = '-' * 46
    script = script.rjust(12, '-')
  print '[%s] %12s %s' % (timestamp, script, filename)


def make_dirs(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)


def remove_dir(directory):
  if os.path.isdir(directory):
    shutil.rmtree(directory)


def clean_files():
  bad_endings = ['pyc', '~']
  print_out(
      'CLEAN FILES',
      'Removing files: %s' % ', '.join(['*%s' % e for e in bad_endings]),
    )
  for home, dirs, files in os.walk(DIR_MAIN):
    for f in files:
      for b in bad_endings:
        if f.endswith(b):
          os.remove(os.path.join(home, f))


def merge_files(source, target):
  fout = open(target, 'a')
  for line in open(source):
    fout.write(line)
  fout.close()


def os_execute(executable, params, source, target, append=False):
  operator = '>>' if append else '>'
  os.system('"%s" %s %s %s %s' % (executable, params, source, operator, target))

def make_lib_zip(force=False):
  if force and os.path.isfile(file_lib):
    os.remove(file_lib)
  if not os.path.isfile(file_lib):
    print_out('ZIP', file_lib)
    shutil.make_archive(dir_lib, 'zip', dir_lib)


def is_dirty(source, target):
  if not os.access(target, os.O_RDONLY):
    return True
  return os.stat(source).st_mtime - os.stat(target).st_mtime > 0

def update_path_separators():
  def fixit(path):
    return path.replace('\\', '/').replace('/', os.sep)

def update_missing_args():
  if args.start:
    args.clean = True


################################################################################
# Main
################################################################################
os.chdir(os.path.dirname(os.path.realpath(__file__)))

update_path_separators()
update_missing_args()

if len(sys.argv) == 1:
  parser.print_help()
  sys.exit(1)

if args.clean:
  print_out('CLEAN')
  clean_files()
  make_lib_zip(force=True)
  remove_dir(dir_dst)
  make_dirs(dir_dst)
  print_out('DONE')

if args.flush:
  remove_dir(dir_storage)
  print_out('STORAGE CLEARED')

if args.start:
  make_dirs(dir_storage)
  clear = 'yes' if args.flush else 'no'
  port = int(args.port)
  run_command = '''
      dev_appserver.py %s
      --host %s
      --port %s
      --admin_port %s
      --storage_path=%s
      --clear_datastore=%s
      --skip_sdk_update_check
    ''' % (DIR_MAIN, args.host, port, port + 1, dir_storage, clear)
  os.system(run_command.replace('\n', ' '))
