import pytest

from config.api_config import ApiUrls
from request_response.request.gorest import GoRest
from utilities.api_calls_utils import FrameworkUtils
from utilities.common_utils import CommonUtility


@pytest.mark.IntegrationTest
def test_api_workflow():
    #Adding User using Post API
    random_email = CommonUtility.get_unique_email()
    create_user = GoRest.CREATE_USER
    create_user['email'] = random_email
    GET_HEADER = CommonUtility.get_custom_header()
    GET_USER_URL = ApiUrls.GET_USER
    post_response = FrameworkUtils.fire_api_with_custom_headers(request_method="POST", request_url=GET_USER_URL,
                                                           request_json=create_user, headers=GET_HEADER,
                                                           expected_status_code=201)
    print(post_response.json())
    user_id = post_response.json()['id']
    print(user_id)

    #Get the User using GET Api
    GET_USER_BY_ID = ApiUrls.get_user_by_id(user_id=12345)
    GET_HEADER = CommonUtility.get_custom_header()
    get_response = FrameworkUtils.fire_api_with_custom_headers(request_url=GET_USER_BY_ID,
                                                           headers=GET_HEADER,
                                                           )
    print(get_response.json())
    assert post_response.json()['email'] == get_response.json()['email'], "API Validation is not successfull"
    print("Integration Testing is PASSED")
