#!/usr/bin/python

import argparse
from pprint import pprint
import os
import re

def ProcessTable(Table, Exclude, Tables):
	if not Tables:
		return True

	if Exclude:
		return not Table in Tables
	else:
		return Table in Tables

parser = argparse.ArgumentParser(description='Extract some tables from a MySQL database dump file into individual files')
parser.add_argument('--tables', '-t', metavar='table', nargs='+', help='Tables to include or exclude (if none specified, will include all tables)')
parser.add_argument('sql', help='The SQL file to be used as input')
parser.add_argument('--exclude', '-x', action='store_true', help='If specified, the list of tables will be treated as an include list, rather than an exclude list')

args = parser.parse_args()

SQLFile = args.sql
Exclude = args.exclude
Tables = args.tables

if SQLFile and os.path.isfile(SQLFile):
	print 'Will process ' + SQLFile

	with open(SQLFile) as InFile:
		pattern = re.compile('DROP TABLE IF EXISTS `(.*)`;')
		OutFile = None

		for Line in InFile:
			if Line.startswith('UNLOCK TABLES;'):
				if OutFile:
					OutFile.write(Line)
					OutFile.close()
					OutFile = None
			else:
				Match = pattern.search(Line)

				if Match:
					TableName = Match.group(1)

					if ProcessTable(TableName, Exclude, Tables):
						OutFile = open(TableName+'.sql', 'w')
						print 'Processing ' + TableName

			if OutFile:
				OutFile.write(Line)
else:
	print SQLFile + ' not found'

