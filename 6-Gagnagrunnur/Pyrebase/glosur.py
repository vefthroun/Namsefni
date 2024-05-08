
#sign in
"""
email=input('enter your email')
password=input('enter your password')
try:
    author.sign_in_with_email_and_password(email,password)
    print('succesfully signed in')
except:
    print('Invalid email or password')
"""
#register
"""
email=input('enter your email')
password=input('enter your password')
confirmpsw=input('confirm your password')
if password==confirmpsw:
    try:
        author.create_user_with_email_and_password(email,password)
        print('Sucsessfully registered')
    except:
        print('Sorry - Email exist')
"""
# Database CRUD
# Create
"""
gogn={  'Fyrirsögn':'Köttur út í mýri, annar kafli',
        'Pistill':'Lokaþulur við íslensk ævintýri eru fjölbreytilegar og oft koma sömu hendingarnar fyrir í mismunandi samböndum, þar á meðal þessar. Dæmi um slíkar þulur má finna í þjóðsagnasafni Jóns Árnasonar.',
        'Höfundur':'Jón Árnason',
        'Dagsetning':'03.10.22'
        }
db.child('pistlar').push(gogn)
"""
# Update
"""
postar=db.child('pistlar').get()
for post in postar.each():
    if post.val()['Höfundur']=='Jón Árnason':
        db.child('pistlar').child(post.key()).update({'Fyrirsögn':'Köttur út í mýri, endir'})
        print(post.key())
        print(post.val())
"""
# Delete
"""
postar=db.child('pistlar').get()
for post in postar.each():
    if post.val()['Höfundur']=='Páll Jónsson':
        db.child('pistlar').child(post.key()).remove()
    #print(person.val())
"""
# Read (from -KEY note)
"""
postur=db.child('pistlar').child('-NDUc1XbUT8ubvJlt7tG').get()
print(postur.val())
"""
# Write 
""" 
postur=db.child('pistlar').get()
for post in postur.each():
    if post.val()['Höfundur']=='Jón Árnason':
        db.child('pistlar').push({
        'Fyrirsögn':'Mýrin',
        'Pistill':'Það var einu sinni köttur sem hét Stýri út í mýri sem setti sig upp á móti öllum og úti er ævintýri',
        'Höfundur':'Páll Jónsson',
        'Dagsetning':'04.10.22'
        })
"""
# kvikmyndir.is api usr: Gjg1801 psw: 1234567gjg