# -*- coding: utf-8 -*-


def generate_grid_response(
        total,
        payload={}):
    """
        Generates json response
    """
    response_json = {'total': total, 'records': payload}

    return response_json


def generate_success_response(
        total,
        payload={}):
    """
        Generates json response for successful operation
    """
    return generate_grid_response(total=total,
                                  payload=payload)
