#!/usr/bin/env python
"""
This module contains reusable reporting functions.  """

import getopt
import re
import datetime


def parse_args(argv):
    # Parse CLI input #
    arg_dict = dict()

    # Initialize global arg defaults.
    # These will override defaults in other scripts so limit to basic values only supplied in CLI
    # The resulting arg_dict is merged in other scripts to override script/local defaults
    arg_dict['cookbook'] = False
    arg_dict['env'] = False
    arg_dict['usage'] = False

    try:
        opts, args = getopt.getopt(argv, "c:e:E:hs:")
    except getopt.GetoptError:
        usage(2)
    for opt, arg in opts:
        if opt == '-c':
            arg_dict['cookbook'] = arg
        elif opt == '-e':
            arg_dict['time_end'] = arg
        elif opt == '-E':
            arg_dict['env'] = arg
        elif opt == '-h':
            arg_dict['usage'] = True
        elif opt == '-s':
            arg_dict['time_start'] = arg
    return arg_dict

def epoch_offset(epoch, offset):
    if offset == 'now':
        return epoch
    m = re.match(r"[-]?(\d+)m$", offset)
    if m:
        val = int(m.group(1))
        epoch = epoch - (val * 60)
        return epoch
    m = re.match(r"[-]?(\d+)h$", offset)
    if m:
        val = int(m.group(1))
        epoch = epoch - (val * 60 * 60)
        return epoch
    m = re.match(r"[-]?(\d+)d$", offset)
    if m:
        val = int(m.group(1))
        epoch = epoch - (val * 24 * 60 * 60)
        return epoch

