#!/usr/bin/python

class AWSMetrics:
    api_key = None
    api_secret = None
    ec2_conn = None
    cloudwatch_conn = None

    def __init__(self, api_key=None, api_secret=None):
	# Initializing the AWS account with key and secret
	if api_key and api_secret:
	    self.api_key = api_key
	    self.api_secret = api_secret
	else:
	    print "API Key and API Secret is missing - Kindly Check !!!"
	    return None

    def get_ec2_conn(self):
	# Connecting to the EC2 instances 
	if self.ec2_conn:
	    return self.ec2_conn
	else:
	    from boto.ec2.connection import EC2Connection
	    try:
		self.ec2_conn = EC2Connection(self.api_key, self.api_secret)
		return self.ec2_conn
	    except:
		print "Wrong API KEY and SECRET - Unable to connect"
		return None

    def get_cloudwatch_conn(self):
    	
    	
 if __name__ == "__main__":
    ACCESS_KEY='AKIAJ4H7QY35TCYBPIRA'
    SECRET='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'
    aws_object = AWSMetrics(ACCESS_KEY, SECRET)
    aws_object.get_current_instances()
    aws_object.get_volumes_attached()
    aws_object.get_disk_usage()
    
