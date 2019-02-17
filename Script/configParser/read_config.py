import configparser

config = configparser.ConfigParser()
print(config.sections())

config.read('sample.ini')
print(config.sections())  #['bitbucket.org', 'topsecret.server.com', 'akseth.com']

print('bitbucket.org' in config) # True

print('bytebong.com' in config) # False

print(config['bitbucket.org']['User']) #'hg'

print(config['DEFAULT']['Compression']) #'yes'

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11']) # 'no'
print(topsecret['Port']) #'50022'


for key in config['bitbucket.org']:  
    print(key)

# user
# compressionlevel
# serveraliveinterval
# compression
# forwardx11
print(config['bitbucket.org']['ForwardX11']) #'yes'

for key in config['akseth.com']:
    print(key)

# blog
# serveraliveinterval
# compression
# compressionlevel
# forwardx11


