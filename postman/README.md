# Postman Collection

A Postman collection is a group of HTTP requests that can be saved and exported to share with other individuals. 

In this case I’ve created a collection that contains three steps that will help us through the upload process. Here’s a brief explanation of each one of them.

### Step 1: Check DO on device

API endpoint that allows us to verify the device is ready to receive the JSON file with all of its configuration. 
We should excpect a ```HTTP/200 OK```.

##### Configuration
* Update Authorization with the correct username/password. Use basic type.
* Make sure we're ignoring SSL errors (we're connecting to the IP). 

### Step 2: Push Config to Device
API endpoint that pushes the configuration to the device contained in the request's body.
We should not execute this step more than once.

##### Configuration
* Update Authorization with the correct username/password. Use basic type.
* Under ```body``` select type ```raw``` and paste the JSON with the F5 device configuration in it.
* Make sure we're ignoring SSL errors (we're connecting to the IP).

### Step 3: Check progress
API endpoint that check the installation progress. It usually takes around 3 minutes for the installation to be done. 
We should expect ```HTTP/200 OK```. 

##### Configuration
* Update Authorization with the correct username/password. Use basic type.
* Make sure we're ignoring SSL errors (we're connecting to the IP).