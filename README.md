# CMPE273-AWS-Project

The Screen looks similar to this :
![ScreenShot](/screenshots/awsConsoleScreenshot.png)

<pre>

Installation and execution

•	First Install Node.js and npm
•	Clone the repository
•	Install all the dependencies
•	npm install
•	Place a security certificate and a private key in a folder named "security". Now you need to get a certificate from a CA or create a       self-signed certificate using OpenSSL.
    openssl genrsa -out privatekey.pem 1024
    openssl req -new -key privatekey.pem -out certrequest.csr
    openssl x509 -req -in certrequest.csr -signkey privatekey.pem -out certificate.pem
•	Run the server
•	node server.js
•	Put IP address of the remote server in your browser, or just type in 'localhost' if you are testing this on your personal machine. Now you should see a web page ready to accept your AWS login.

</pre>
