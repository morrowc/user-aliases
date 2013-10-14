#!/usr/bin/python
"""Create a new alias file, which contains only the users on this host.

author: chris+github@as701.net
"""
import os
import re
from optparse import OptionParser

def MakeSubAliases(users, alias, maxlen):
  """Turn a long list of usernames into several sub aliases.

  Args:
    users: a list, of usernames.
    alias: a string, the alias name.
    maxlen: an integer, how long a sub aliase can be.

  Returns:
    a dict of: {'subalias': [user1, user2, user3]}
  """
  result = {}
  # Create temporary lists to append to results-dict of maxlen items.
  for mark in xrange(len(users)/maxlen):
    result['%s-%02d' % (alias, mark)] = users[mark*maxlen:mark*maxlen+maxlen]

  # Add the remainder items to the results.
  u = len(users)
  remainder = (u % maxlen) * -1
  result['%s-%02d' % (alias, mark+1)] = users[remainder:]
  return result


def UserList():
  """List all users on the system.

  Returns:
    a list of usernames on the system.
  """
  return(sorted(os.listdir('/home')))


def main():
  opts = OptionParser()
  opts.add_option('-a', '--alias', dest='alias', default='mach-users',
                  help='What final alias name to create.')

  opts.add_option('-m', '--max_len', dest='max_len', default=10,
                  help='How many usernames on a sub alias.')

  opts.add_option('-o', '--outfile', dest='outfile', default='user-alias',
                  help='Name of the output alias file.')

  (options, args) = opts.parse_args()

  aliases = MakeSubAliases(UserList(), options.alias, options.max_len)
  for al in sorted(aliases):
    print '%s: %s' % (al, ','.join(sorted(aliases[al])))

  print '%s: %s' % (options.alias, ','.join(sorted(aliases)))

if __name__ == '__main__':
  main()
