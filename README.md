# flask-demo-service
An example for a service created with flask which controls connections to a resource.


## Installing and running the service:

1. Make sure you have Docker Desktop installed by running the command `docker --version` in the terminal. 
   not receiving the version back means Docker is not installed.
   Get it here: https://www.docker.com/products/docker-desktop 

2. Clone the repository using HTTP:
`git clone https://github.com/omrigee/flask-demo-service.git`
     or
download the files from:
 https://github.com/omrigee/flask-demo-service to a directory.

3. Go to repository directory
   `cd flask-demo-service`

4. Enter the following command:
   `docker run -i -t -p 7800:5000 flask-demo-service`.
  This command will start the service on port 7800.
    

## Using the service:

  There are 20 initiallized resources. 
  their identifiers are from `127.0.5.1` to `127.0.5.20`
  
  Once your'e done installing and initiallizing the service as explained in the previous section, you can use it. 

  To *receive* a resource, go to: 
  http://localhost:7800/users/ip

  for example, going to 
  http://localhost:7800/users/127.0.5.6
  returns resource username and password, and locks him. 

  
  To *release* a resource, send the following POST HTTP request to
   http://localhost:7800/users/ 
   
   :

   {
    “Ip”:127.0.5.1”
   }

   in example, will release the 127.0.5.1 resource.


   
