import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from hello.py import form_data

fromaddr = "twitterfreeze@gmail.com"
toaddr = form_data["email"]
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TwitterFreeze_Analysis"
 
body = """
Hi there, you just downloaded your tweets and here is your analysis!
Have Fun!

Best wishes,
Twitter Freeze
"""

if form_data = "on" 
	
	msg.attach(MIMEText(body, 'plain'))
    
	filename_rd = "form_data.txt"
	filename_an = "analysis.pdf"
	attachment_rd = open("https://github.com/nicolabrant/twitter-freeze/form_data.txt", "rb")
	attachment_an = open("https://github.com/nicolabrant/twitter-freeze/analysis.pdf", "rb")
 
	part_rd = MIMEBase('application', 'octet-stream')
	part_rd.set_payload((attachment_rd).read())

	part_an = MIMEBase('application', 'octet-stream')
	part_rd.set_payload((attachment_an).read())

	encoders.encode_base64(part_rd)
	encoders.encode_base64(part_an)

	part_rd.add_header('Content-Disposition', "attachment; filename= %s" % filename_rd, )
 
	msg.attach(attachment_rd)
	msg.attach(attachment_an)
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "twitfree")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

else:

	msg.attach(MIMEText(body, 'plain'))
    
	filename = "analysis.pdf"
	attachment = open("https://github.com/nicolabrant/twitter-freeze/analysis.pdf", "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename, )
 
	msg.attach(part)
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "twitfree")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()