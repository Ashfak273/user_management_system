""" All the http request functionality

This file can also be imported as service and contains the following functionality
    * get_request - http get call with all functionality
    * post_request - http post call with all functionality
"""
import requests
from app.config.logging_config import get_logger

logger = get_logger(class_name=__name__)


class HttpService:
    @classmethod
    def get_request(cls, url: str, query_params: dict = None, headers: dict = None, auth_enable=False):
        """ Http get call with all functionality
        Parameters
        ----------
        url: str
            Http get call url
        query_params: dict
            Get call query parameters
        headers: dict
            Get call headers
        auth_enable: bool
            JWT authentication enable or disable status

        Returns
        ----------
        tuple:
            Response object as JSON object, Http status
        """
        logger.info("Http Get Request Started")
        logger.debug(f"URL: {url}, Params: {query_params}, Headers: {headers}")
        response = requests.get(url=url, params=query_params, headers=headers)
        logger.debug(f"Response Code: {response.status_code}, Response Payload: {response.text}")
        logger.info("Http Get Request End")
        return response.json(), response.status_code

    @classmethod
    def post_request(cls, url: str, query_params: dict = None, payload: any = None, headers: dict = None,
                     auth_enable=False):
        """ Http post call with all functionality
        Parameters
        ----------
        url: str
            Http get call url
        query_params: dict
            Get call query parameters
        payload: any
            Post call request body
        headers: dict
            Get call headers
        auth_enable: bool
            JWT authentication enable or disable status

        Returns
        ----------
        tuple:
            Response object as JSON object, Http status
        """
        logger.info("Http Post Request Started")
        logger.debug(f"URL: {url}, Params: {query_params}, Headers: {headers}")
        response = requests.post(url=url, params=query_params, json=payload, headers=headers)
        logger.debug(f"Response Code: {response.status_code}, Response Payload: {response.text}")
        logger.info("Http Post Request End")
        return response.json(), response.status_code
