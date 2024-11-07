import pytest

from config.api_config import ApiUrls
from function_api_test.functional_param import FunctionalParam
from request_response.request.gorest import GoRest
from utilities import common_utils
from utilities.api_calls_utils import FrameworkUtils
from utilities.common_utils import CommonUtility


def test_testUrl():
    url = FunctionalParam.get_base_end_point()
    print("url is ", url)


def test_user_url():
    GET_USER_URL = ApiUrls.GET_USER
    print("GET USER URL", GET_USER_URL)


def test_user_url_by_id():
    GET_USER_URL_BY_ID = ApiUrls.get_user_by_id("123456")
    print("Get user url by Id is ", GET_USER_URL_BY_ID)


def test_header():
    GET_HEADER = CommonUtility.get_custom_header()
    print("Header is ", GET_HEADER)


def get_unique_email():
    random_email = CommonUtility.get_unique_email()
    print(random_email)


def get_json_request():
    create_user = GoRest.CREATE_USER
    print("Create User Request is ", create_user)
    update_user = GoRest.UPDATE_USER
    print("Update User Request is ", update_user)

@pytest.mark.GET
def test_get_API():
    url = FunctionalParam.get_base_end_point()
    GET_HEADER = CommonUtility.get_custom_header()
    GET_USER_URL = ApiUrls.GET_USER
    response = FrameworkUtils.fire_api_with_custom_headers("GET",request_url = GET_USER_URL, headers = GET_HEADER)
    print(response.json())
@pytest.mark.POST
def test_post_API():
    random_email = CommonUtility.get_unique_email()
    create_user = GoRest.CREATE_USER
    create_user['email'] = random_email
    GET_HEADER = CommonUtility.get_custom_header()
    GET_USER_URL = ApiUrls.GET_USER
    response = FrameworkUtils.fire_api_with_custom_headers(request_method= "POST", request_url= GET_USER_URL, request_json= create_user, headers= GET_HEADER, expected_status_code=201)
    print(response.json())




# test_testUrl()
# test_user_url()
# test_user_url_by_id()
# test_header()
# get_unique_email()
# get_json_request()

