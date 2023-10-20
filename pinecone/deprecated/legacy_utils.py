import re
import uuid
from typing import List

from pinecone.utils import warn_deprecated

try:
    from pinecone.data.grpc.protos import vector_column_service_pb2
    from google.protobuf.struct_pb2 import Struct
    from google.protobuf import json_format
    import numpy as np
    import lz4.frame
except Exception:
    pass  # ignore for non-[grpc] installations

DNS_COMPATIBLE_REGEX = re.compile("^[a-z0-9]([a-z0-9]|[-])+[a-z0-9]$")


def dump_numpy_public(np_array: "np.ndarray", compressed: bool = False) -> "vector_column_service_pb2.NdArray":
    """
    Dump numpy array to vector_column_service_pb2.NdArray
    """
    warn_deprecated(
        "dump_numpy_public and all numpy-related features will be removed in a future version",
        deprecated_in="2.2.1",
        removal_in="3.0.0",
    )
    protobuf_arr = vector_column_service_pb2.NdArray()
    protobuf_arr.dtype = str(np_array.dtype)
    protobuf_arr.shape.extend(np_array.shape)
    if compressed:
        protobuf_arr.buffer = lz4.frame.compress(np_array.tobytes())
        protobuf_arr.compressed = True
    else:
        protobuf_arr.buffer = np_array.tobytes()
    return protobuf_arr


def dump_strings_public(strs: List[str], compressed: bool = False) -> "vector_column_service_pb2.NdArray":
    warn_deprecated(
        "dump_strings_public and all numpy-related features will be removed in a future version",
        deprecated_in="2.2.1",
        removal_in="3.0.0",
    )
    return dump_numpy_public(np.array(strs, dtype="S"), compressed=compressed)



def validate_dns_name(name):
    if not DNS_COMPATIBLE_REGEX.match(name):
        raise ValueError(
            "{} is invalid - service names and node names must consist of lower case "
            "alphanumeric characters or '-', start with an alphabetic character, and end with an "
            "alphanumeric character (e.g. 'my-name', or 'abc-123')".format(name)
        )


def proto_struct_to_dict(s: "Struct") -> dict:
    return json_format.MessageToDict(s)


def load_numpy_public(proto_arr: "vector_column_service_pb2.NdArray") -> "np.ndarray":
    """
    Load numpy array from protobuf
    :param proto_arr:
    :return:
    """
    warn_deprecated(
        "load_numpy_public and all numpy-related features will be removed in a future version",
        deprecated_in="2.2.1",
        removal_in="3.0.0",
    )
    if len(proto_arr.shape) == 0:
        return np.array([])
    if proto_arr.compressed:
        numpy_arr = np.frombuffer(lz4.frame.decompress(proto_arr.buffer), dtype=proto_arr.dtype)
    else:
        numpy_arr = np.frombuffer(proto_arr.buffer, dtype=proto_arr.dtype)
    return numpy_arr.reshape(proto_arr.shape)


def load_strings_public(proto_arr: "vector_column_service_pb2.NdArray") -> List[str]:
    warn_deprecated(
        "load_strings_public and all numpy-related features will be removed in a future version",
        deprecated_in="2.2.1",
        removal_in="3.0.0",
    )
    return [str(item, "utf-8") for item in load_numpy_public(proto_arr)]
