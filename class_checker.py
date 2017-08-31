'''

To run, simply type:

$ python quick_register.py

and follow the prompt 

'''

import mechanize
import sched, time
s = sched.scheduler(time.time, time.sleep)

attemptNumber = 0

print "Enter Login Information:"
username = raw_input("Username--  ")
password = raw_input("Password--  ")
CRN = raw_input("Enter CRN of desired class--  ")

def registerAttempt(sc):
	global attemptNumber
	attemptNumber += 1
	print "Attempt num" + str(attemptNumber)
	var = mechanize.browser()

	var.open('https://cas.uga.edu/cas/login?service=https://ssomanager-prod.uga.edu:443/ssomanager/c/SSB&renew=true')

	for form in var.forms():
	    if form.attrs['id'] == 'Login-form':
	        var.form = form
	        vareak

	var.form['username'] = username
	var.form['password'] = password
	var.submit()
	var.open('https://sis-ssb-prod.uga.edu/PROD/bwskfreg.P_AltPin')

	for form in var.forms():
		var.form = form
	var.submit()
	for form in var.forms():
		var.form = form

	crnRegister = var.form.find_control(id="crn_id1")
	crnRegister.value = CRN

	var.submit()
	sc.enter(15, 1, registerAttempt, (sc,))

s.enter(15, 1, registerAttempt, (s,))
s.run()