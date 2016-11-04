# -*-coding:utf-8 -*-
__author__ = 'hubble'
import optparse

parser = optparse.OptionParser(description="Query the stock's value.", usage="%prog [-f] [-q]", version="%prog 1.0")
parser.add_option("-f", "--file", action="print_file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print(options.filename)
print(options.verbose)
print(args)



