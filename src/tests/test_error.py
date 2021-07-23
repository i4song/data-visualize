from . import *


@pytest.mark.parametrize('error_code', [
    400, 403
])
def test_error_handler(flask_client, error_code):
    res = flask_client.get
    assert res.status_code == error_code
