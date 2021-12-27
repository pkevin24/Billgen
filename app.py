from flask import Flask,render_template,request
from flask.globals import request
# import smtplib  # python library to send emails
from flask_mail import Mail, Message
# recipient = input("Enter Email of the Recipient:\n") #receives mail address
app = Flask(__name__,template_folder='Template')
mail = Mail(app)
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'demo24062000@gmail.com'
app.config['MAIL_PASSWORD'] = 'kvhebbal'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
def SendEmailq(recipient,amt,name):
    msg = Message(
				'BILL AMOUNT',
				sender ='demo24062000@gmail.com',
				recipients = [recipient]
			)
    SUBJECT = ""
    amt1=str(amt)
    msg.body = "Hello "+ name+"\n\tThankyou for using our smart power extender. You will have to pay Rs "+amt1+" for these many amout of consumption.\n\tYou can pay the amout by any of the following ways. \n\tHope you use our extender again. Seeyaa"
    mail.send(msg)
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
    SendEmailq(email,amt,name)
    # l={'name':name,'email':email,'hr':hr}
    return render_template('billout.html',name1=name,email1=email,hr1=hr)
    

if __name__=="__main__":
    app.run(debug=True)
