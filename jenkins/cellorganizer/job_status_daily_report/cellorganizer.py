% Author: Ivan Cao-Berg
%
% Copyright (C) 2014 Murphy Lab
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published
% by the Free Software Foundation; either version 2 of the License,
% or (at your option) any later version.
%
% This program is distributed in the hope that it will be useful, but
% WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
% General Public License for more details.
%
% You should have received a copy of the GNU General Public License
% along with this program; if not, write to the Free Software
% Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
% 02110-1301, USA.
%
% For additional information visit send email to icaoberg@gmail.com

try:
	from jenkins import Jenkins
except:
	print "Unable to import jenkins"
	print "pip install python-jenkins"
	exit()

try:
	from tabulate import tabulate
except:
	print "Unable to import tabulate"
	print "pip install tabulate"
	exit()

from datetime import datetime

def get_status( status_color ):
	if status_color in 'blue':
		return 'SUCCESS'
	elif status_color in 'red':
		return 'FAILURE'
	elif status_color in 'gray':
		return 'NEVER TESTED'
	elif status_color in 'disabled':
		return 'DISABLED'
	elif status_color in 'aborted':
		return 'ABORTED'
	else:
		return status_color.upper()

def main():
	print "This is automated report generated by icaoberg@developers.compbio.cs.cmu.edu on " + datetime.now().strftime("%Y-%m-%d %H:%M")

	address = 'http://developers.compbio.cs.cmu.edu:8080'
	j = Jenkins(address)
	jobs = j.get_jobs()

	print '------------------------'
	print 'CellOrganizer for Matlab'
	print '------------------------'

	success_table = []
	failure_table = []
	other_table = []
	successes = 0
	failures = 0
	for job in jobs:
		if 'cellorganizer-demo3D' in job['name'] or 'cellorganizer-demo2D' in job['name']:
			status = get_status(job['color'])
			if status == 'SUCCESS':
				successes += 1
				success_table.append([job['name'], status])
			elif status == 'FAILURE':
				failures += 1
				failure_table.append([job['name'], status])
			else:
				other_table.append([job['name'], status])

	print "\nSuccessful Jobs Table"
	print tabulate(success_table, headers=["Name","Status"], tablefmt='grid')

	print "\nFailed Jobs Table"
	print tabulate(failure_table, headers=["Name","Status"], tablefmt='grid')

	if '++\n++' != tabulate(other_table, headers=["Name","Status"], tablefmt='grid'):
		print "\nOther Jobs"
		print tabulate(other_table, headers=["Name","Status"], tablefmt='grid')

	print "\nNumber of Total Successes: " + str(successes)
	print "Number of Total Failures " + str(failures)

	print '\n\n------------------------'
	print 'CellOrganizer for Python'
	print '------------------------'

	success_table = []
	failure_table = []
	other_table = []
	successes = 0
	failures = 0
	for job in jobs:
		if 'cellorganizer' in job['name'] and 'python' in job['name']:
			status = get_status(job['color'])
			if status == 'SUCCESS':
				successes += 1
				success_table.append([job['name'], status])
			elif status == 'FAILURE':
				failures += 1
				failure_table.append([job['name'], status])
			else:
				other_table.append([job['name'], status])

	print "\nSuccessful Jobs Table"
	print tabulate(success_table, headers=["Name","Status"], tablefmt='grid')

	print "\nFailed Jobs Table"
	print tabulate(failure_table, headers=["Name","Status"], tablefmt='grid')

	if '++\n++' != tabulate(other_table, headers=["Name","Status"], tablefmt='grid'):
		print "\nOther Jobs"
		print tabulate(other_table, headers=["Name","Status"], tablefmt='grid')

	print "\nNumber of Total Successes: " + str(successes)
	print "Number of Total Failures " + str(failures)

if __name__ == "__main__":
    main()
