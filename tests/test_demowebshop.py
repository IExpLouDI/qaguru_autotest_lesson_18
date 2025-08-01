import allure
from selene import have, browser, be


def test_should_be_log_in(setup_browser):
    with allure.step('Перезагружаем главную страницу'):
        setup_browser.open('https://demowebshop.tricentis.com')
    with allure.step('Проверяем что пользователь авторизован'):
        setup_browser.element('.account').should(have.text('demoqa@test.su'))


def test_check_shopping_cart(setup_browser:browser, add_item, clean):
    with allure.step('Открываем корзину'):
        setup_browser.open('https://demowebshop.tricentis.com/cart')
    with allure.step('В корзине находится "Build your own cheap computer"'):
        setup_browser.element('.product-name').should(have.text('Build your own cheap computer'))
    with allure.step('Проверка количества товара'):
        setup_browser.element(f".qty input[value='{add_item}']").should(be.present_in_dom)
