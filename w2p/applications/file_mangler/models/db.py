# -*- coding: utf-8 -*- 

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    session.connect(request, response, db=db) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db=MEMDB(Client())
else:
    db = DAL('sqlite://storage.sqlite')                           # else use a normal relational database
##db = DAL('mysql://root:life@localhost:1234/filemanager')       # if not, use SQLite or other DB
## if no need for session
# session.forget()

#########################################################################
## Here is sample code if you need for 
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## comment/uncomment as needed

from gluon.tools import *
auth=Auth(globals(),db)                      # authentication/authorization
auth.settings.hmac_key='sha512:83facfee-eaa5-4e27-9c31-6c4adfbc2e7f'
auth.define_tables()                         # creates all needed tables
crud=Crud(globals(),db)                      # for CRUD helpers using auth
service=Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc

# crud.settings.auth=auth                      # enforces authorization on crud
# mail=Mail()                                  # mailer
# mail.settings.server='smtp.gmail.com:587'    # your SMTP server
# mail.settings.sender='you@gmail.com'         # your email
# mail.settings.login='username:password'      # your credentials or None
# auth.settings.mailer=mail                    # for user email verification
# auth.settings.registration_requires_verification = True
# auth.settings.registration_requires_approval = True
# auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['verify_email'])+'/%(key)s to verify your email'
# auth.settings.reset_password_requires_verification = True
# auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['reset_password'])+'/%(key)s to reset your password'
## more options discussed in gluon/tools.py
#########################################################################

#########################################################################
## Define your tables below, for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
import datetime
now=datetime.datetime.now()
if auth.is_logged_in():
   me=auth.user.id
else:
   me=None

db.define_table('allfiles',
    Field('filename'),
    Field('filepath'),
    Field('parentpath'),
    Field('filetype'),
    Field('file','upload'),
    Field('content','text'),
    Field('datecreated','datetime',default=now),
    Field('datemodified','datetime',default=now),
    Field('filesize','integer'),
    Field('user',db.auth_user,default=me))

db.define_table('test_detail',
    Field('Corp','text'),
    Field('Address_1','text'),
    Field('Address_2','text'),
    Field('City','text'),
    Field('State','text'),
    Field('Country','text'),
    Field('Postal_Code','text'),
    Field('Requester','text'),
    Field('Code_1','text'),
    Field('Role','text'),
    Field('Asset_Groups','text'),
    Field('IPs','text'),
    Field('Active_Hosts','integer'),
    Field('Hosts_Matching_Filters','integer'),
    Field('Trend_Analysis','text'),
    Field('Date_Range','text'),
    Field('Asset_Tags','text'))

db.define_table('qid_def',
    Field('QID','text'),
    Field('CVE_ID','text'),
    Field('Vendor_Reference','text'),
    Field('Bug_Traq','text'),
    Field('CVSS','float'),
    Field('CVSS_Base','float'), 
    Field('CVSS_Temporal','float'),
    Field('Threat','text'),
    Field('Impact','text'),
    Field('Solution','text'),
    Field('Exploitability','text'),
    Field('Associated_Malware','text'),
    Field('PCI_Vuln','text'))
