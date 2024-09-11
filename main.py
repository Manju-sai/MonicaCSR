import datetime
import os
import smtplib
from email.mime.text import MIMEText
from flask import render_template, session, redirect, url_for
import firebase_admin
import random
from flask import Flask, request
from firebase_admin import credentials, firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
app=Flask(__name__)
app.secret_key="CRS_Portal@1234"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = '/static/upload'

sender = "ujjwala0903@gmail.com"
password = "ecwgfrrlrkdmnrts"

events=['Environmental Responsibility','Ethical Responsibility','Philonthropic Responsibility','Economic Responsibility','Others']
locations=['Bangalore','Mangalore','Mysore','Mumbai']

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

@app.route('/')
def homepage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/usermainpage')
def usermainpage():
    try:
        return render_template("usermainpage.html")
    except Exception as e:
        return str(e)

@app.route('/index')
def indexpage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/logout')
def logoutpage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/about')
def aboutpage():
    try:
        return render_template("about.html")
    except Exception as e:
        return str(e)

@app.route('/logout')
def logout():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/adminmainpage')
def adminmainpage():
    try:
        return render_template("adminmainpage.html")
    except Exception as e:
        return str(e)

@app.route('/services')
def servicespage():
    try:
        return render_template("services.html")
    except Exception as e:
        return str(e)

@app.route('/types')
def typespage():
    try:
        return render_template("types.html")
    except Exception as e:
        return str(e)

@app.route('/environmentpage')
def environmentpage():
    try:
        return render_template("environmentpage.html")
    except Exception as e:
        return str(e)

@app.route('/ethicalpage')
def ethicalpage():
    try:
        return render_template("ethicalpage.html")
    except Exception as e:
        return str(e)

@app.route('/philanthropicpage')
def philanthropicpage():
    try:
        return render_template("philanthropicpage.html")
    except Exception as e:
        return str(e)

@app.route('/economicpage')
def economicpage():
    try:
        return render_template("economicpage.html")
    except Exception as e:
        return str(e)

@app.route('/gallery')
def gallerypage():
    try:
        return render_template("gallery.html")
    except Exception as e:
        return str(e)

@app.route('/adminviewstaffs')
def adminviewstaffspage():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newstaff')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data " , data)
        return render_template("adminviewstaffs.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewusers')
def adminviewuserspage():
    try:
        db = firestore.client()
        dbref = db.collection('newuser')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data ", data)
        return render_template("adminviewusers.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewusers')
def staffviewusers():
    try:
        db = firestore.client()
        dbref = db.collection('newuser')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data ", data)
        return render_template("staffviewusers.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewcontacts')
def adminviewcontacts():
    try:
        db = firestore.client()
        dbref = db.collection('newcontact')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print(data)
        return render_template("adminviewcontacts.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/userviewownevents')
def userviewownevents():
    try:
        userid= session['userid']
        db = firestore.client()
        dbref = db.collection('newevent')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if(temp['UserId']==userid):
                data.append(doc.to_dict())
        print(data)
        return render_template("userviewownevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/userviewallevents')
def userviewallevents():
    try:
        userid = session['userid']
        db = firestore.client()
        dbref = db.collection('newevent')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['UserId'] != userid):
                data.append(doc.to_dict())
        return render_template("userviewallevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewevents')
def adminviewevents():
    try:
        db = firestore.client()
        dbref = db.collection('newevent')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            data.append(doc.to_dict())
        return render_template("adminviewevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewevents')
def staffviewevents():
    try:
        db = firestore.client()
        dbref = db.collection('newevent')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            data.append(doc.to_dict())
        return render_template("staffviewevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewreports')
def adminviewreports():
    try:
        #userid = session['userid']
        db = firestore.client()
        dbref = db.collection('newresponse')
        dbdata = dbref.get()
        data = []
        for doc in dbdata:
            data.append(doc.to_dict())
        pie_data = []
        for x in events:
            cnt=0
            for doc in dbdata:
                temp = doc.to_dict()
                if(temp['EventType']==x):
                    cnt+=1
            if(cnt>0):
                tempdata = {"label": x, "y": cnt}
                pie_data.append(tempdata)
        print("Graph Data : ", pie_data)
        return render_template("adminviewreports.html", data=data, pie_data=pie_data)
    except Exception as e:
        return str(e)

@app.route('/staffviewreports')
def staffviewreports():
    try:
        #userid = session['userid']
        db = firestore.client()
        dbref = db.collection('newresponse')
        dbdata = dbref.get()
        data = []
        for doc in dbdata:
            data.append(doc.to_dict())
        data_points = []
        for x in events:
            cnt=0
            for doc in dbdata:
                temp = doc.to_dict()
                if(temp['EventType']==x):
                    cnt+=1
            if(cnt>0):
                tempdata = {"label": x, "y": cnt}
                data_points.append(tempdata)
        return render_template("staffviewreports.html", data=data, data_points=data_points)
    except Exception as e:
        return str(e)

@app.route('/userviewresponses')
def userviewresponses():
    try:
        #userid = session['userid']
        id=request.args['id']
        db = firestore.client()
        dbref = db.collection('newresponse')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['EventId'] == id):
                data.append(doc.to_dict())
        return render_template("userviewresponses.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewresponses')
def adminviewresponses():
    try:
        #userid = session['userid']
        id=request.args['id']
        db = firestore.client()
        dbref = db.collection('newresponse')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['EventId'] == id):
                data.append(doc.to_dict())
        return render_template("adminviewresponses.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewresponses')
def staffviewresponses():
    try:
        #userid = session['userid']
        id=request.args['id']
        db = firestore.client()
        dbref = db.collection('newresponse')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['EventId'] == id):
                data.append(doc.to_dict())
        return render_template("staffviewresponses.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminlogin',methods=["POST","GET"])
def adminloginpage():
    try:
        print('hi')
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            if uname == "admin" and pwd == "admin":
                return render_template("adminmainpage.html")
            else:
                return render_template("adminlogin.html", msg="UserName/Password is Invalid")
        return render_template("adminlogin.html",msg="")
    except Exception as e:
        return str(e)

@app.route('/userlogincheck', methods=['POST'])
def userlogincheck():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            print("Uname : ", uname, " Pwd : ", pwd);
            newdb_ref = db.collection('newuser')
            dbdata = newdb_ref.get()
            data = []
            flag = False
            for doc in dbdata:
                #print(doc.to_dict())
                #print(f'{doc.id} => {doc.to_dict()}')
                #data.append(doc.to_dict())
                data = doc.to_dict()
                if(data['UserName']==uname and data['Password']==pwd):
                    flag=True
                    session['userid']=data['id']
                    break
            if(flag):
                print("Login Success")
                return render_template("usermainpage.html")
            else:
                return render_template("userlogin.html", msg="UserName/Password is Invalid")
    except Exception as e:
        return render_template("userlogin.html", msg=e)

@app.route('/stafflogincheck', methods=['POST'])
def stafflogincheck():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            print("Uname : ", uname, " Pwd : ", pwd);
            newdb_ref = db.collection('newstaff')
            dbdata = newdb_ref.get()
            data = []
            flag = False
            for doc in dbdata:
                data = doc.to_dict()
                if(data['UserName']==uname and data['Password']==pwd):
                    flag=True
                    session['staffid']=data['id']
                    break
            if(flag):
                print("Login Success")
                return render_template("staffmainpage.html")
            else:
                return render_template("stafflogin.html", msg="UserName/Password is Invalid")
    except Exception as e:
        return render_template("stafflogin.html", msg=e)

@app.route('/userlogin',methods=["POST","GET"])
def userloginpage():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            newdb_ref = db.collection('newuser')
            dbdata = newdb_ref.get()
            flag = False
            for doc in dbdata:
                data = doc.to_dict()
                if (data['UserName'] == uname and data['Password'] == pwd):
                    flag = True
                    session['userid'] = data['id']
                    break
            if (flag):
                print("Login Success")
                return render_template("usermainpage.html")
            else:
                return render_template("userlogin.html", msg="UserName/Password is Invalid")
        return render_template("userlogin.html")
    except Exception as e:
        return str(e)

@app.route('/stafflogin',methods=["POST","GET"])
def staffloginpage():
    try:
        return render_template("stafflogin.html")
    except Exception as e:
        return str(e)

@app.route('/newuser',methods=["POST","GET"])
def newuser():
    try:
        msg=""
        if request.method == 'POST':
            print("Add New User page")
            fname = request.form['fname']
            lname = request.form['lname']
            uname = request.form['uname']
            pwd = request.form['pwd']
            email = request.form['email']
            phnum = request.form['phnum']
            address = request.form['address']
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'FirstName': fname,'LastName':lname,
                    'UserName': uname,'Password':pwd,
                    'EmailId': email,'PhoneNumber':phnum,
                    'Address': address}
            db = firestore.client()
            newuser_ref = db.collection('newuser')
            id = json['id']
            newuser_ref.document(id).set(json)
            msg="New User Added Success"
            return render_template("newuser.html", msg=msg)
        else:
            return render_template("newuser.html", msg=msg)
    except Exception as e:
        return str(e)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/newstaff', methods=['POST',"GET"])
def newstaff():
    try:
        msg=""
        return render_template("adminaddstaff.html", msg=msg)
    except Exception as e:
        return str(e)

@app.route('/adminaddstaff', methods=['POST',"GET"])
def adminaddstaff():
    try:
        msg=""
        if request.method == 'POST':
            print("Add New Staff page")
            fname = request.form['fname']
            lname = request.form['lname']
            uname = request.form['uname']
            pwd = request.form['pwd']
            email = request.form['email']
            phnum = request.form['phnum']
            address = request.form['address']
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'FirstName': fname,'LastName':lname,
                    'UserName': uname,'Password':pwd,
                    'EmailId': email,'PhoneNumber':phnum,
                    'Address': address}
            db = firestore.client()
            newuser_ref = db.collection('newstaff')
            id = json['id']
            newuser_ref.document(id).set(json)
            msg="New Staff Added Success"
            return render_template("adminaddstaff.html", msg=msg)
        else:
            return render_template("adminaddstaff.html", msg=msg)
    except Exception as e:
        return str(e)

@app.route('/userapplyresponse', methods=['POST',"GET"])
def userapplyresponse():
    try:
        id=request.args['id']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newevent')
        data = newdb_ref.document(id).get().to_dict()
        return render_template("userapplyresponse.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("userapplyresponse.html", msg=e)

@app.route('/userapplyresponse1', methods=['POST',"GET"])
def userapplyresponse1():
    try:
        msg=""
        if request.method == 'POST':
            print("Add Response to a Event page")
            eid = request.form['eid']
            ename = request.form['ename']
            etype = request.form['etype']
            location = request.form['location']
            description = request.form['description']
            email = request.form['email']
            phnum = request.form['phnum']
            edate = request.form['edate']
            userid = session['userid']
            comments = request.form['comments']

            id = str(random.randint(1000, 9999))
            json = {'id': id, 'EventId':eid,
                    'EventName': ename,'EventType':etype,
                    'Description': description,'Location':location,
                    'ContactEmailId': email,'ContactPhoneNumber':phnum,
                    'UserId': userid,'EventDate':edate, 'Comments':comments}
            db = firestore.client()
            newdb_ref = db.collection('newresponse')
            id = json['id']
            newdb_ref.document(id).set(json)
            print("Add New Response Added")
            userid = session['userid']
            newdb_ref = db.collection('newuser')
            data = newdb_ref.document(userid).get().to_dict()
            subject="Event Notification"
            fname = data['FirstName']
            lname = data['LastName']
            body = "A User "+fname + " " + lname + " sent a response please login & check"
            recipients = []
            recipients.append(email)
            print(recipients)
            send_email(subject, body, sender, recipients, password)
            msg="New Response to a Event Added Success"
            db = firestore.client()
            newdb_ref = db.collection('newevent')
            data = newdb_ref.document(eid).get().to_dict()
            return render_template("userapplyresponse.html", data=data, msg=msg)
        else:
            return render_template("userapplyresponse.html", msg=msg)
    except Exception as e:
        return str(e)

@app.route('/useraddevents', methods=['POST',"GET"])
def useraddevents():
    try:
        msg=""
        current_date = datetime.date.today()
        if request.method == 'POST':
            print("Add New Event page")
            ename = request.form['ename']
            etype = request.form['etype']
            location = request.form['location']
            description = request.form['description']
            email = request.form['email']
            phnum = request.form['phnum']
            edate = request.form['edate']
            userid = session['userid']
            print("Add New Event page")
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'EventName': ename,'EventType':etype,
                    'Description': description,'Location':location,
                    'ContactEmailId': email,'ContactPhoneNumber':phnum,
                    'UserId': userid,'EventDate':edate}
            db = firestore.client()
            newdb_ref = db.collection('newevent')
            id = json['id']
            newdb_ref.document(id).set(json)
            msg="New Event Added Success"
            return render_template("useraddevents.html", msg=msg, events=events, locations=locations,
                                   current_date=current_date)
        else:
            return render_template("useraddevents.html", msg=msg, events=events, locations=locations,
                                   current_date=current_date)
    except Exception as e:
        return str(e)

@app.route('/contact',methods=['POST','GET'])
def contactpage():
    try:
        msg=""
        if request.method == 'POST':
            cname = request.form['cname']
            email = request.form['emailid']
            subject = request.form['subject']
            message = request.form['message']
            phone = request.form['phnum']
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'ContactName': cname,
                    'Message': message, 'Subject': subject,
                    'EmailId': email, 'PhoneNumber':phone}
            db = firestore.client()
            db_ref = db.collection('newcontact')
            id = json['id']
            db_ref.document(id).set(json)
            msg="Contact Added Success"
        return render_template("contact.html",msg=msg)
    except Exception as e:
        return str(e)

@app.route('/userviewprofile')
def userviewprofile():
    try:
        id=session['userid']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newuser')
        data = newdb_ref.document(id).get().to_dict()
        return render_template("userviewprofile.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("userviewprofile.html", msg=e)

@app.route('/staffviewprofile')
def staffviewprofile():
    try:
        id=session['staffid']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newstaff')
        data = newdb_ref.document(id).get().to_dict()
        print(data)
        return render_template("staffviewprofile.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("stafflogin.html", msg=e)

if __name__ == '__main__':
    app.run(debug=True)