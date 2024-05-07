import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth  
from pprint import pprint

#default_app = firebase_admin.initialize_app() 

# Fetch the service account key JSON file contents (root)
cred = credentials.Certificate('verk5demo-serviceAccount.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://verk5demo-default-rtdb.europe-west1.firebasedatabase.app'
})

############################ Authentication #################################

'''user = auth.create_user(
    email='user@example.com',
    email_verified=False,
    phone_number='+15555550100',
    password='secretPassword',
    display_name='John Doe',
    photo_url='http://www.example.com/12345678/photo.png',
    disabled=False)
print('Sucessfully created new user: {0}'.format(user.uid))'''

# ná í user ID og birta email
'''uid = 'CwSVcjqJKaRZNYx7scfxt1zMKuK2'
user = auth.get_user(uid)
pprint('Successfully fetched user data: {0}'.format(user.email))'''

# ná í email og birta uid
'''email = 'user@example.com'
user = auth.get_user_by_email(email)
print('Successfully fetched user data: {0}'.format(user.uid))'''

############################### Reatime database ##################################
# The app only has access as defined in the Security Rules = auth.uid !== null
 
dbref = db.reference('mailbox')

#read
#pprint(dbref.get())

#write
'''dbref.push({
    "name":"Anna Jóns",
    "title":"Fyrsta fyrirsögnin",
    "content":"Þetta er fyrsta færslan í töflunni",
    "timestamp":"ptime",
    "userId":"localId"
})'''
#set
'''dbref.child('-NxCqMpcyPVF8xuRh16P').set({
    "name":"Anna",
    "title":"Fyrirsögnin er breytt",
    "content":"færslan í töflunni hefur verið breytt",
    "timestamp":"ptime",
    "userId":"localId"
})'''
#update
'''dbref.child('-NxCqMpcyPVF8xuRh16P').update({
    "name":"Anna Panna",
    "title":"Fyrirsögnin er breytt aftur",
    "content":"færslan í töflunni hefur verið uppfærð eða þannig",
})'''
#delete
#dbref.child('-NxIbO5WmE5uSPKrnaA_').delete()