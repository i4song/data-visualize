from . import *


def test_server_run(flask_app):
    app = flask_app
    assert app is not None


@pytest.mark.parametrize('env, expected',
        [
            ('dev', 'Development'),
            ('prod', 'Product'),
            ('test', 'Testing')
        ]
)
def test_server_env(env, expected):
    app = create_app(env)
    assert app.config['MESSAGE'] == expected
