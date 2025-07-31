import pytest
from selene import browser
import requests as rq


@pytest.fixture(scope='session')
def get_cookie():
    request_body = {'Email': 'demoqa@test.su',
                    'Password': 'qwe123',
                    'RememberMe': False}

    response = rq.post(url='https://demowebshop.tricentis.com/login',
                       data=request_body, allow_redirects=False)
    return response.cookies.get('NOPCOMMERCE.AUTH')


@pytest.fixture(scope='session')
def setup_browser(get_cookie):

    browser.open('https://demowebshop.tricentis.com')
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH",
                               "value": get_cookie,
                               "domain": "demowebshop.tricentis.com"}
                              )
    return browser


@pytest.fixture(scope='session')
def setup_session(get_cookie):
    session = rq.session()
    session.cookies.set('NOPCOMMERCE.AUTH',get_cookie , domain='demowebshop.tricentis.com')
    return session

@pytest.fixture()
def add_item(setup_session):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'ru',
    }
    payload = ("product_attribute_72_5_18=53&product_attribute_72_6_19=54&product_attribute_72_3_20=57"
                         "&addtocart_72.EnteredQuantity=1")
    setup_session.post(url='https://demowebshop.tricentis.com/addproducttocart/details/72/1',headers=headers, data=payload)

    return True

