from flask import Flask,render_template,request
from flask.globals import request
import smtplib,ssl  # python library to send emails

# recipient = input("Enter Email of the Recipient:\n") #receives mail address
# def SendEmail(recipient,amt,name):
#     server = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 = port number
#     server.ehlo() # check the smtp connection 
#     server.starttls()  # start the conection 
#     server.login("demo24062000@gmail.com" , "kvhebbal") 
#     SUBJECT = "BILL AMOUNT"
#     amt1=str(amt)
#     message = 'Subject: {}\n\n{}'.format(SUBJECT,"Hello "+ name+"\n\tThankyou for using our smart power extender. You will have to pay Rs "+amt1+" for these many amout of consumption.\n\tYou can pay the amout by any of the following ways. \n\tHope you use our extender again. Seeyaa")
#     server.sendmail("demo24062000@gmail.com" , recipient , message)
#     server.close() 


def SendEmail(recipient,amt,name):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "demo24062000@gmail.com"  # Enter your address
    receiver_email = recipient  # Enter receiver address
    password = "vbkxwlwyjlpmonuu"
    SUBJECT = "BILL AMOUNT"
    # name="Kevin"
    amt1=str(amt)
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    message = 'Subject: {}\n\n{}'.format(SUBJECT,"Hello "+ name+"\n\tThankyou for using our smart power extender. You will have to pay Rs "+amt1+" for these many amout of consumption.\n\tYou can pay the amout by any of the following ways. \n\tHope you use our extender again. Seeyaa")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

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
    # check()
    SendEmail(email,amt,name)
    # l={'name':name,'email':email,'hr':hr}
    return render_template('billout.html',name1=name,email1=email,hr1=hr)
    

if __name__=="__main__":
    app.run(debug=True)
