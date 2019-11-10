'''
Matthew Ragan | matthewragan.com
'''
import socket
import json

ComClass = mod("comEXT").Com

class Job(ComClass):
	'''
		This is a bare bones Communcation class.

		This sample class has several important features that can be described here.


		Notes
		---------------
		Your notes about the class go here
 	'''

	def __init__(self, myOp):
		self.MyOp 			= myOp

		ComClass.__init__(self, myOp)
		
		print("Job Class init")
		pass

	def SendHb(self, msg):
		op.Heartbeat.SendHb(msg)
		pass
	
	def HbResponse(self, msg):
		op.Heartbeat.HbResponse(msg)
		pass