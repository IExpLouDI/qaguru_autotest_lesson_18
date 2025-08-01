import json

import allure
from allure_commons.types import AttachmentType


def add_response_attach(response):
    allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")


def add_response_cookies(response):
    allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")


def add_authorization_attach_body(response):
    allure.attach(body=str(response.request.body), name='RequestBody', attachment_type=AttachmentType.TEXT,
                  extension='txt')


def add_authorization_attach_headers(response):
    allure.attach(body=json.dumps(dict(response.request.headers), ensure_ascii=False),
                  name='RequestHEADERS', attachment_type=AttachmentType.JSON)
