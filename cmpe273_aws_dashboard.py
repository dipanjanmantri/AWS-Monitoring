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
	    
	    
    def get_current_instances(self):
	try:
	    conn = self.get_ec2_conn()
	    reservations = conn.get_all_instances()
	    instances = [i for r in reservations for i in r.instances]
	    for i in instances:
		print "InstanceId:%s, Instance Type: %s, Launch Time: %s, Ip Address: %s, Public DNS Name: %s" %(i.id, i.instance_type, i.launch_time, i.ip_address, i.public_dns_name)
	except Exception, e:
	    print e
	    
	    

	    
if __name__ == "__main__":
    ACCESS_KEY='AKIAJ4H7QY35TCYBPIRA'
    SECRET='izxv5KO6O8hazTDeGZV8gUUarWNsXF9UUo3DGEIR'
    aws_object = AWSMetrics(ACCESS_KEY, SECRET)
    print "Gettings all the servers which are present in your account "
    aws_object.get_current_instances()
   
  
