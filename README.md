# random-user-api
Create an API that generates n number of random users on a JSON object

## Configure a Python virtual environment and install chalice
<code>
virtualenv -p `which python3` venv3 <br>
source venv3/bin/activate <br>
pip install chalice
</code>
<br>Note that the above command uses a backtick character (`) and <i>not</i> a single quote character (')

## Create a new project called random-user-api
<code>
chalice new-project random-user-api
</code>

## Deploy the API locally and test
<code>
chalice local<br>
curl -X GET http://localhost:80000
</code>

## Deploy to API Gateway
<code>
chalice deploy
</code>
<br>

You should now have an API deployed in AWS that responds to a GET request. You can now develop with this API and run <code>chalice deploy</code> when needed to deploy changes.