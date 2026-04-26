from api.users_api import UsersAPI
from utils.validators import *
from utils.test_data import get_new_user
import time



def test_get_users(api_context):
    users_api = UsersAPI(api_context)

    response = users_api.get_users()
    validate_status(response, 200)

    data = response.json()
    assert isinstance(data, list)  # response should be list of users


def test_create_user(api_context):
    users_api = UsersAPI(api_context)
    payload = get_new_user()

    response = users_api.create_user(payload)
    validate_status(response, 201)

    data = response.json()
    validate_user_schema(data)  # validate required fields


def test_get_user_by_id(api_context):
    users_api = UsersAPI(api_context)
    payload = get_new_user()

    create_res = users_api.create_user(payload)
    user_id = create_res.json()["id"]  # dynamic ID

    response = users_api.get_user_by_id(user_id)
    validate_status(response, 200)


def test_update_user(api_context):
    users_api = UsersAPI(api_context)
    payload = get_new_user()

    create_res = users_api.create_user(payload)
    user_id = create_res.json()["id"]

    updated_payload = {"name": "Updated Name"}

    response = users_api.update_user(user_id, updated_payload)
    # print(response.text())  # debug response

    validate_status(response, 200)
    assert response.json()["name"] == "Updated Name"  # verify update


def test_delete_user(api_context):
    users_api = UsersAPI(api_context)
    payload = get_new_user()

    create_res = users_api.create_user(payload)
    user_id = create_res.json()["id"]

    response = users_api.delete_user(user_id)  # use dynamic ID
    assert response.status in [200, 204]


def test_get_users_performance(api_context):
    users_api = UsersAPI(api_context)

    start_time = time.time()  # start timer

    response = users_api.get_users()

    end_time = time.time()  # end timer

    response_time = (end_time - start_time) * 1000  # convert to ms

    print(f"Response Time: {response_time} ms")

    assert response.status == 200
    assert response_time < 2000, f"Slow API! Took {response_time} ms"
    