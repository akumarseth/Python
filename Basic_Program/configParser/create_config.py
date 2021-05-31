import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                      'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

config['akseth.com'] = {}
config['akseth.com']['blog'] = 'http://akseth.blogspot.in'

with open('sample.ini', 'w') as configfile:
   config.write(configfile)

