from selene import have, browser


def test_should_be_log_in(add_item, setup_browser):
    setup_browser.element('.account').should(have.text('demoqa@test.su'))


def test_check_shopping_cart(setup_browser:browser, add_item):
    setup_browser.open('https://demowebshop.tricentis.com/cart')
    setup_browser.element('.product-name').should(have.text('Build your own cheap computer'))