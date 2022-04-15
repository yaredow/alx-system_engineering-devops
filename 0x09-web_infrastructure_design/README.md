https://imgur.com/UFzkSld.png

Visual representation of LAMP stack with:
1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

What is a server?
A server is a piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called "clients".

What is the role of the domain name?
Domain Names are the unique name that identifies an entity, whether that be an single individual or a company, on the Internet. 

What type of DNS record www is in www.foobar.com?
CNAME

What is the role of the application server?
To serve and handle business logic to application programs and all application operatios between users and an organizations backend business applications or databases

What is the role of the database?
To store, maintain  and organize information/data so that it can be easily accessed, updated and managed.

What is the server using to communicate with the computer of the user requestings the website?
HTTP

issues are with this infrastructure:
SPOF: Since there is only one server, if that server fails, the entire system will stop working

Downtime when maintenance needed (like deploying new code web server needs to be restarted)

Cannot scale if too much incoming traffic

