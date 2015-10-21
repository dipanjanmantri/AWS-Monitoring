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
	# Connecting with cloudwatch
	if self.cloudwatch_conn:
	    return self.cloudwatch_conn
	else:
		# boto amazon aws sdk for connecting with AWS
	    import boto
	    try:
		self.cloudwatch_conn = boto.connect_cloudwatch(self.api_key, self.api_secret)
		return self.cloudwatch_conn
	    except:
		print "Wrong API KEY, SECRET combination - Unable to get the cloudwatch connection"
		return None


	# Function to get all the instances 
    def get_current_instances(self):
	try:
	    conn = self.get_ec2_conn()
	    reservations = conn.get_all_instances()
	    instances = [i for r in reservations for i in r.instances]
	    for i in instances:
		print "InstanceId:%s, Instance Type: %s, Launch Time: %s, Ip Address: %s, Public DNS Name: %s" %(i.id, i.instance_type, i.launch_time, i.ip_address, i.public_dns_name)
	except Exception, e:
	    print e


	# Function to get Volume attached
    def get_volumes_attached(self):
	conn = self.get_ec2_conn()
	volumes = conn.get_all_volumes()
	for x in volumes:
	    print "VolumeId:%s, Volume Size:%s GB, Volume region: %s, Status: %s" %(x.id, x.size, x.region, x.status)



    
	
if __name__ == "__main__":
    ACCESS_KEY='AKIAJ4H7QY35TCYBPIRA'
    SECRET='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'
    aws_object = AWSMetrics(ACCESS_KEY, SECRET)
    print "*************************************************************"
    print "Gettings all the servers which are present in your account "
    aws_object.get_current_instances()
    print "*************************************************************"
    print "\n\n\n\nGetting the details of the Volumes(Disk) that are attached to the servers:"
    aws_object.get_volumes_attached()
    print "*************************************************************"
    print "\n\n\n\nGetting the disk usages of the volumes now...:"
    aws_object.get_disk_usage()
    print "*************************************************************"
