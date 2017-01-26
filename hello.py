#!/usr/bin/env python

#^ this thing is called the "shebang"
import os
import json
import cgi
import Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])

if username =="Tuxin" and password == "Zhang":
    print "Set-Cookie: loggedin=true"

print "Content-Type: text/html"
print 
print "<HTML><BODY>"
print "<H1>Hello World !</H1>"
print "Your magic tracking number is : "
print form.getvalue('magic_tracking_number')
print "<p>Your browser is :"
if "Firefox" in os.environ['HTTP_USER_AGENT']:
    print "Firefox !"
elif "chrome" in os.environ['HTTP_USER_AGENT']:
    print "Chrome !"    
else:
    print os.environ['HTTP_USER_AGENT']
        
print "<FORM method='POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>"

    
print "<p>Username : "+ str(username)
print "<p>Password : "+ str(password)
if username =="Tuxin" and password == "Zhang":
    print "<p>Login Successful !"
if 'loggedin' in C:
    print "<p>Logged In: " + str(C['loggedin'].value)
else:
    print "<p> No Cookie"
    
    
    
    
#print json.dumps(dict(os.environ),indent=2,sort_keys = True)



