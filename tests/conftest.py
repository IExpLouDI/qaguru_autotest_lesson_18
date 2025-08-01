import allure
import pytest
from selene import browser
import requests as rq

from utils.attachments import add_response_attach, add_response_cookies, add_authorization_attach_body, \
    add_authorization_attach_headers


@pytest.fixture(scope='session')
def get_cookie():
    with allure.step('Авторизация пользователя через API'):
        request_body = {'Email': 'demoqa@test.su',
                        'Password': 'qwe123',
                        'RememberMe': False}

        response = rq.post(url='https://demowebshop.tricentis.com/login',
                           data=request_body, allow_redirects=False)
        add_authorization_attach_body(response)
        add_authorization_attach_headers(response)
    add_response_cookies(response)

    return response.cookies.get('NOPCOMMERCE.AUTH')


@pytest.fixture(scope='function')
def setup_browser(get_cookie):

    browser.open('https://demowebshop.tricentis.com')
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH",
                               "value": get_cookie,
                               "domain": "demowebshop.tricentis.com"}
                              )
    return browser


@pytest.fixture(scope='session')
def setup_session(get_cookie):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'ru',
    }
    session = rq.session()
    session.cookies.set('NOPCOMMERCE.AUTH',get_cookie , domain='demowebshop.tricentis.com')
    session.headers=headers
    return session


@pytest.fixture(params=['1', '10', '10000'])
def add_item(setup_session, request):
    with allure.step(f'Добавить в корзину товар в количестве - {request.param}'):
        payload = (f"product_attribute_72_5_18=53&product_attribute_72_6_19=54&product_attribute_72_3_20=57"
                             f"&addtocart_72.EnteredQuantity={request.param}")
        response = setup_session.post(url='https://demowebshop.tricentis.com/addproducttocart/details/72/1', data=payload)

    add_response_attach(response)

    yield request.param


@pytest.fixture()
def clean():
    yield
    with allure.step('Зачистка корзины'):
        browser.element('.qty-input').clear().type(0)
        browser.element("[name='updatecart']").click()
