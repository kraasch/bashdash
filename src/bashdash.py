#!/usr/bin/python3

import subprocess
import argparse
import os
import pathlib

# constant variables.
program_name='bashdash'

# get path to project.
bin_path = pathlib.Path(__file__)
# if needed follow symlinks.
while os.path.islink(bin_path):
    bin_path=os.readlink(bin_path) # follow the link.
    bin_path=pathlib.Path(bin_path) # convert str to Path.
dashboard_root=bin_path.parent.parent / 'dashboards'

# parse arguments.
parser = argparse.ArgumentParser(prog=program_name)
parser.add_argument('-d', '--dashboard', help='Run a dashboard.', type=str)
parser.add_argument('-l', '--list',      action='store_true', help='Show all dashboards.')
args = parser.parse_args()
dashboard_file=str(args.dashboard) + '.yml'
dashboard_path=str(dashboard_root / dashboard_file)

# execute dashboard.
if args.list:
    rc = subprocess.call(['ls', '-1', str(dashboard_root)])
    exit()

if args.dashboard:
    # exit if file does not exist.
    if not os.path.exists(dashboard_path):
        print(f"dashboard does not exist: '{dashboard_path}'.")
        exit()
    rc = subprocess.call(['sampler', '--config', dashboard_path])
    exit()

