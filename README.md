## Deloitte API
------
Welcome to this small API created for a second round of a job interview at Deloitte Netherlands. The goal of the API is to return a company's name with a copyright symbol. The two endpoints are described below. The API can be found at [http://api.obdam.xyz/](http://api.obdam.xyz/) or [http://15.236.219.94/](http://15.236.219.94/).

### Main endpoint **GET** `/`
Simple webpage displaying a "_Hey World_".

### Copyright symbol endpoint **POST** `/api/companies/copyrighted`
Send a JSON POST request to the API which contains one or more companies in a string which need the copyright symbol added. Example:
```JSON
{
    "input": "We, at Deloitte, really like the new security features of Google Cloud."
}
```