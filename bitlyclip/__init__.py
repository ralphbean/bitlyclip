#!/usr/bin/env python

import os
import sys
import optparse
from ConfigParser import ConfigParser

import bitlyapi

pynotify = None
try:
    import pynotify
    pynotify.init('bitlyclip')
except ImportError, e:
    pass

def notify(message, cls='dialog-message'):
    print message
    if not pynotify:
        return False
    notif = pynotify.Notification("bitlyclip", message, cls)
    return notif.show()

def parse_args():
    p = optparse.OptionParser()
    p.add_option('-f', '--config', default='~/.bitly')
    return p.parse_args()

def main(url):
    opts, args = parse_args()

    config = ConfigParser()
    config.read(os.path.expanduser(opts.config))

    if not config.has_section('bitly'):
        msg = 'Failed to read bit.ly API configuration ' \
              'from %s.' % opts.config
        notify("%s failed.\n%s" % (__file__, msg), 'dialog-warning')
        sys.exit(1)

    api = bitlyapi.BitLy(
            config.get('bitly', 'api_user'),
            config.get('bitly', 'api_key'),
            )

    return api.shorten(longUrl=url)['url']

def cmd():
    try:
        #Copy from the clipboard
        url = os.popen('xsel').read()

        #BitLy magic
        short_url = main(url)

        #Paste to the clipboard
        os.popen('xsel -i', 'wb').write(short_url)
        notify('%s\n\n\tshortened to\n\n%s\n\n' % (url, short_url) +
               '\t(and put in your clipboard)')
    except Exception, e:
        notify("%s failed.\n%s" % (__file__, str(e)), 'dialog-warning')
