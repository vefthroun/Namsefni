from flask import Flask

import pyrebase
from pyrebase.pyrebase import Auth

import os

app = Flask(__name__)

#os.urandom(8) fyrir csrf og session
app.secret_key = os.urandom(8)

config = {
  "apiKey": "............",
  "authDomain": "............",
  "databaseURL":"............",
  "projectId":"............",
  "storageBucket":"............",
  "messagingSenderId":"............",
  "appId":"............",
  "measurementId":"............"
}
firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()

storage=firebase.storage()
# upload
filename=input("Enter the name of the file you want to upload: ")
# where
cloudfilename=input("Enter the folder/name of the file in the cloud: ")
# put
storage.child(cloudfilename).put(filename)
# get url
print(storage.child(cloudfilename).get_url(None))

# download file from FB
#cloudfilename=input("Enter the folder/name of the file you want to download: ")
#storage.child(cloudfilename).download("","notes/dwnl.txt")

# read file from FB
'''cloudfilename=input("Enter the folder/name of the file you want to read: ")
url=storage.child(cloudfilename).get_url(None)
file=urllib.request.urlopen(url).read()

print(file)'''

'''if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  '''