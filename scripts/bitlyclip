#!/usr/bin/env python

import os
import sys
import optparse
from ConfigParser import ConfigParser

import bitlyapi

def parse_args():
    p = optparse.OptionParser()
    p.add_option('-f', '--config', default='~/.bitly')
    return p.parse_args()

def main(url):
    opts, args = parse_args()

    config = ConfigParser()
    config.read(os.path.expanduser(opts.config))

    if not config.has_section('bitly'):
        print >>sys.stderr, 'Failed to read bit.ly API configuration ' \
                'from %s.' % opts.config
        sys.exit(1)

    api = bitlyapi.BitLy(
            config.get('bitly', 'api_user'),
            config.get('bitly', 'api_key'),
            )

    res = api.shorten(longUrl=url)
    return res['url']

if __name__ == '__main__':
    #Copy from the clipboard
    import os
    url = os.popen('xsel').read()

    #BitLy magic
    url = main(url)

    #Paste to the clipboard
    import os
    os.popen('xsel', 'wb').write(url)
