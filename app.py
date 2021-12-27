from flask import Flask,render_template,request
from flask.globals import request
# import smtplib  # python library to send emails
# from flask import Flask
from flask_mail import Mail, Message

# recipient = input("Enter Email of the Recipient:\n") #receives mail address
def SendEmail(rec,a1,name1):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    me = "demo24062000@gmail.com"
    my_password = r"kvhebbal"
    you = rec
    name=name1
    amt1=str(a1)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Bill Amount"
    msg['From'] = me
    msg['To'] = you
    m1="Hello "+ name+"\n\tThankyou for using our smart power extender. You will have to pay Rs "+str(amt1)+" for these many amout of consumption.\nYou can pay the amout by any of the following ways. \n\tHope you use our extender again. Seeyaa"
    part2 = MIMEText(m1)
    
    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()
app = Flask(__name__,template_folder='Template')
@app.route("/")
def billfeed():
    return render_template('bill.html')
# @app.route("/details")
@app.route("/amount",methods=['POST','GET'])
def bill():
    rate=10.5
    name=request.form['Name']
    email=request.form['Email']
    hr=request.form['Hrs']
    amt=rate*float(hr)
#     SendEmail(email,amt,name)
    # l={'name':name,'email':email,'hr':hr}
    return render_template('billout.html',name1=name,email1=email,hr1=hr)
    

if __name__=="__main__":
    app.run(debug=True)
