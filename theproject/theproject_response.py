# -*- coding: utf-8 -*-


def generate_response(
        success,
        msg,
        payload = {},
        err_code= None):
    """
        Generates json response
    """
    response_json = {'success': success, 'message': msg, 'payload': payload}

    if not success:
        if err_code:
            response_json['error_code'] = err_code

    return response_json


def generate_success_response(
        msg_dict,
        payload= {}):

    """
        Generates json response for successful operation
    """
    return generate_response(success=True,
                             msg=msg_dict['message'],
                             payload=payload)