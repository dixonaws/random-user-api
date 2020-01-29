import random
from chalice import Chalice
from faker import Faker

app = Chalice(app_name='random-user-api')

fake = Faker()

# create an API key and usage plan manually in the AWS console
# note: this is possible with the boto3 library
@app.route('/', api_key_required=True)
def index():
    dict_random_user=generate_user()

    # we can simply return a dict object and it will be dumped to json
    return(dict_random_user)


def generate_user():
    dict_user = {}

    str_name = fake.name()
    lst_name = str_name.split()

    dict_user["first_name"] = lst_name[0]
    dict_user["last_name"] = lst_name[1]
    dict_user["address"] = fake.address()

    lst_gender = ["m", "f"]
    dict_user["gender"] = random.choice(lst_gender)

    dict_user["age"] = random.randint(21, 100)

    return (dict_user)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
