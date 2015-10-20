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

  