import os
# TOKEN = '5414229907:AAE1KysoDCr2M_TplHsYJp9AdE0ig0cbzxg'
# TOKEN = '5334753603:AAHZvsUU-6cUGFLFP12Pq9lSv8GKv2gelb4'
PORT = int(os.environ.get('PORT', 5000))
#PORT = 5000
TOKEN = os.environ['TOKEN']
#DATABASE_URL = 'postgresql+psycopg2://xpmeaullcqppxa:d4118cc7a6ed8b075be9ff899c23625cd32d00feb82e17a8ed5348b3a8b268f5@ec2-54-227-248-71.compute-1.amazonaws.com:5432/d3m9nnk01ges0b'
DATABASE_URL = os.environ['DATABASE_URL']
