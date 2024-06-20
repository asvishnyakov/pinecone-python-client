"""
    Pinecone Control Plane API

    Pinecone is a vector database that makes it easy to search and retrieve billions of high-dimensional vectors.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@pinecone.io
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from pinecone.core.client.api_client import ApiClient, Endpoint as _Endpoint
from pinecone.core.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from pinecone.core.client.model.delete_request import DeleteRequest
from pinecone.core.client.model.describe_index_stats_request import DescribeIndexStatsRequest
from pinecone.core.client.model.describe_index_stats_response import DescribeIndexStatsResponse
from pinecone.core.client.model.fetch_response import FetchResponse
from pinecone.core.client.model.list_response import ListResponse
from pinecone.core.client.model.query_request import QueryRequest
from pinecone.core.client.model.query_response import QueryResponse
from pinecone.core.client.model.rpc_status import RpcStatus
from pinecone.core.client.model.update_request import UpdateRequest
from pinecone.core.client.model.upsert_request import UpsertRequest
from pinecone.core.client.model.upsert_response import UpsertResponse


class DataPlaneApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __alt_delete(self, **kwargs):
            """Delete vectors  # noqa: E501

            DEPRECATED. Use [`POST /delete`](https://docs.pinecone.io/reference/delete) instead.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.alt_delete(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                ids ([str]): Vectors to delete.. [optional]
                delete_all (bool): This indicates that all vectors in the index namespace should be deleted.. [optional] if omitted the server will use the default value of False
                namespace (str): The namespace to delete vectors from, if applicable.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.alt_delete = _Endpoint(
            settings={
                "response_type": ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/vectors/delete",
                "operation_id": "alt_delete",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "ids",
                    "delete_all",
                    "namespace",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "ids": ([str],),
                    "delete_all": (bool,),
                    "namespace": (str,),
                },
                "attribute_map": {
                    "ids": "ids",
                    "delete_all": "deleteAll",
                    "namespace": "namespace",
                },
                "location_map": {
                    "ids": "query",
                    "delete_all": "query",
                    "namespace": "query",
                },
                "collection_format_map": {
                    "ids": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__alt_delete,
        )

        def __alt_describe_index_stats(self, **kwargs):
            """Get index stats  # noqa: E501

            DEPRECATED. Use [`POST /describe_index_stats`](https://docs.pinecone.io/reference/describe_index_stats) instead.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.alt_describe_index_stats(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                DescribeIndexStatsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.alt_describe_index_stats = _Endpoint(
            settings={
                "response_type": (DescribeIndexStatsResponse,),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/describe_index_stats",
                "operation_id": "alt_describe_index_stats",
                "http_method": "GET",
                "servers": None,
            },
            params_map={"all": [], "required": [], "nullable": [], "enum": [], "validation": []},
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__alt_describe_index_stats,
        )

        def __delete(self, delete_request, **kwargs):
            """Delete vectors  # noqa: E501

            The `delete` operation deletes vectors, by id, from a single namespace.  For guidance and examples, see [Delete data](https://docs.pinecone.io/docs/delete-data).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete(delete_request, async_req=True)
            >>> result = thread.get()

            Args:
                delete_request (DeleteRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["delete_request"] = delete_request
            return self.call_with_http_info(**kwargs)

        self.delete = _Endpoint(
            settings={
                "response_type": ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/vectors/delete",
                "operation_id": "delete",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "delete_request",
                ],
                "required": [
                    "delete_request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "delete_request": (DeleteRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "delete_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__delete,
        )

        def __describe_index_stats(self, describe_index_stats_request, **kwargs):
            """Get index stats  # noqa: E501

            The `describe_index_stats` operation returns statistics about the contents of an index, including the vector count per namespace and the number of dimensions, and the index fullness.  Serverless indexes scale automatically as needed, so index fullness is relevant only for pod-based indexes.  For pod-based indexes, the index fullness result may be inaccurate during pod resizing; to get the status of a pod resizing process, use [`describe_index`](https://www.pinecone.io/docs/api/operation/describe_index/).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.describe_index_stats(describe_index_stats_request, async_req=True)
            >>> result = thread.get()

            Args:
                describe_index_stats_request (DescribeIndexStatsRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                DescribeIndexStatsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["describe_index_stats_request"] = describe_index_stats_request
            return self.call_with_http_info(**kwargs)

        self.describe_index_stats = _Endpoint(
            settings={
                "response_type": (DescribeIndexStatsResponse,),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/describe_index_stats",
                "operation_id": "describe_index_stats",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "describe_index_stats_request",
                ],
                "required": [
                    "describe_index_stats_request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "describe_index_stats_request": (DescribeIndexStatsRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "describe_index_stats_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__describe_index_stats,
        )

        def __fetch(self, ids, **kwargs):
            """Fetch vectors  # noqa: E501

            The `fetch` operation looks up and returns vectors, by ID, from a single namespace. The returned vectors include the vector data and/or metadata.  For guidance and examples, see [Fetch data](https://docs.pinecone.io/reference/fetch).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetch(ids, async_req=True)
            >>> result = thread.get()

            Args:
                ids ([str]): The vector IDs to fetch. Does not accept values containing spaces.

            Keyword Args:
                namespace (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FetchResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["ids"] = ids
            return self.call_with_http_info(**kwargs)

        self.fetch = _Endpoint(
            settings={
                "response_type": (FetchResponse,),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/vectors/fetch",
                "operation_id": "fetch",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "ids",
                    "namespace",
                ],
                "required": [
                    "ids",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "ids": ([str],),
                    "namespace": (str,),
                },
                "attribute_map": {
                    "ids": "ids",
                    "namespace": "namespace",
                },
                "location_map": {
                    "ids": "query",
                    "namespace": "query",
                },
                "collection_format_map": {
                    "ids": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__fetch,
        )

        def __list(self, **kwargs):
            """List vector IDs  # noqa: E501

            The `list` operation lists the IDs of vectors in a single namespace of a serverless index. An optional prefix can be passed to limit the results to IDs with a common prefix.  `list` returns up to 100 IDs at a time by default in sorted order (bitwise/\"C\" collation). If the `limit` parameter is set, `list` returns up to that number of IDs instead. Whenever there are additional IDs to return, the response also includes a `pagination_token` that you can use to get the next batch of IDs. When the response does not include a `pagination_token`, there are no more IDs to return.  For guidance and examples, see [Get record IDs](https://docs.pinecone.io/docs/get-record-ids).  **Note:** `list` is supported only for serverless indexes.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                prefix (str): The vector IDs to fetch. Does not accept values containing spaces.. [optional]
                limit (int): Max number of ids to return.. [optional]
                pagination_token (str): Pagination token to continue a previous listing operation.. [optional]
                namespace (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.list = _Endpoint(
            settings={
                "response_type": (ListResponse,),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/vectors/list",
                "operation_id": "list",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "prefix",
                    "limit",
                    "pagination_token",
                    "namespace",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "prefix": (str,),
                    "limit": (int,),
                    "pagination_token": (str,),
                    "namespace": (str,),
                },
                "attribute_map": {
                    "prefix": "prefix",
                    "limit": "limit",
                    "pagination_token": "paginationToken",
                    "namespace": "namespace",
                },
                "location_map": {
                    "prefix": "query",
                    "limit": "query",
                    "pagination_token": "query",
                    "namespace": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__list,
        )

        def __query(self, query_request, **kwargs):
            """Query vectors  # noqa: E501

            The `query` operation searches a namespace, using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.  For guidance and examples, see [Query data](https://docs.pinecone.io/docs/query-data).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.query(query_request, async_req=True)
            >>> result = thread.get()

            Args:
                query_request (QueryRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                QueryResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["query_request"] = query_request
            return self.call_with_http_info(**kwargs)

        self.query = _Endpoint(
            settings={
                "response_type": (QueryResponse,),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/query",
                "operation_id": "query",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "query_request",
                ],
                "required": [
                    "query_request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "query_request": (QueryRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "query_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__query,
        )

        def __update(self, update_request, **kwargs):
            """Update a vector  # noqa: E501

            The `update` operation updates a vector in a namespace. If a value is included, it will overwrite the previous value. If a `set_metadata` is included, the values of the fields specified in it will be added or overwrite the previous value.  For guidance and examples, see [Update data](https://docs.pinecone.io/reference/update).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update(update_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_request (UpdateRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["update_request"] = update_request
            return self.call_with_http_info(**kwargs)

        self.update = _Endpoint(
            settings={
                "response_type": ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/vectors/update",
                "operation_id": "update",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "update_request",
                ],
                "required": [
                    "update_request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "update_request": (UpdateRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "update_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__update,
        )

        def __upsert(self, upsert_request, **kwargs):
            """Upsert vectors  # noqa: E501

            The `upsert` operation writes vectors into a namespace. If a new value is upserted for an existing vector ID, it will overwrite the previous value.  For guidance and examples, see [Upsert data](https://docs.pinecone.io/docs/upsert-data).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.upsert(upsert_request, async_req=True)
            >>> result = thread.get()

            Args:
                upsert_request (UpsertRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UpsertResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["upsert_request"] = upsert_request
            return self.call_with_http_info(**kwargs)

        self.upsert = _Endpoint(
            settings={
                "response_type": (UpsertResponse,),
                "auth": ["ApiKeyAuth"],
                "endpoint_path": "/vectors/upsert",
                "operation_id": "upsert",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "upsert_request",
                ],
                "required": [
                    "upsert_request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "upsert_request": (UpsertRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "upsert_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__upsert,
        )
