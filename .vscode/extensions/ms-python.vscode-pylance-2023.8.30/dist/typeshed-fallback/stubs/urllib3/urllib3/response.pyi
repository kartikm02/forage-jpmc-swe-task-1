import io
from collections.abc import Iterable, Iterator, Mapping
from http.client import HTTPMessage as _HttplibHTTPMessage, HTTPResponse as _HttplibHTTPResponse
from typing import IO, Any
from typing_extensions import Literal, Self, TypeAlias

from urllib3.connectionpool import HTTPConnection

from . import HTTPConnectionPool, Retry
from ._collections import HTTPHeaderDict

_TYPE_BODY: TypeAlias = bytes | IO[Any] | Iterable[bytes] | str

class DeflateDecoder:
    def __getattr__(self, name: str) -> Any: ...
    def decompress(self, data: bytes) -> bytes: ...

class GzipDecoderState:
    FIRST_MEMBER: Literal[0]
    OTHER_MEMBERS: Literal[1]
    SWALLOW_DATA: Literal[2]

class GzipDecoder:
    def __getattr__(self, name: str) -> Any: ...
    def decompress(self, data: bytes) -> bytes: ...

# This class is only available if
# `brotli` is available for import.
class BrotliDecoder:
    def flush(self) -> bytes: ...

class MultiDecoder:
    def __init__(self, modes: str) -> None: ...
    def flush(self) -> bytes: ...
    def decompress(self, data: bytes) -> bytes: ...

class HTTPResponse(io.IOBase):
    CONTENT_DECODERS: list[str]
    REDIRECT_STATUSES: list[int]
    headers: HTTPHeaderDict
    status: int
    version: int
    reason: str | None
    strict: int
    decode_content: bool
    retries: Retry | None
    enforce_content_length: bool
    auto_close: bool
    msg: _HttplibHTTPMessage | None
    chunked: bool
    chunk_left: int | None
    length_remaining: int | None
    def __init__(
        self,
        body: _TYPE_BODY = "",
        headers: Mapping[str, str] | Mapping[bytes, bytes] | None = None,
        status: int = 0,
        version: int = 0,
        reason: str | None = None,
        strict: int = 0,
        preload_content: bool = True,
        decode_content: bool = True,
        original_response: _HttplibHTTPResponse | None = None,
        pool: HTTPConnectionPool | None = None,
        connection: HTTPConnection | None = None,
        msg: _HttplibHTTPMessage | None = None,
        retries: Retry | None = None,
        enforce_content_length: bool = False,
        request_method: str | None = None,
        request_url: str | None = None,
        auto_close: bool = True,
    ) -> None: ...
    def get_redirect_location(self) -> Literal[False] | str | None: ...
    def release_conn(self) -> None: ...
    def drain_conn(self) -> None: ...
    @property
    def data(self) -> bytes | Any: ...
    @property
    def connection(self) -> HTTPConnection | Any: ...
    def isclosed(self) -> bool: ...
    def tell(self) -> int: ...
    def read(self, amt: int | None = None, decode_content: bool | None = None, cache_content: bool = False) -> bytes: ...
    def stream(self, amt: int | None = 65536, decode_content: bool | None = None) -> Iterator[bytes]: ...
    @classmethod
    def from_httplib(cls, r: _HttplibHTTPResponse, **response_kw: Any) -> Self: ...
    def getheaders(self) -> HTTPHeaderDict: ...
    def getheader(self, name, default=None) -> str | None: ...
    def info(self) -> HTTPHeaderDict: ...
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def readable(self) -> bool: ...
    def readinto(self, b: bytearray) -> int: ...
    def supports_chunked_reads(self) -> bool: ...
    def read_chunked(self, amt: int | None = None, decode_content: bool | None = None) -> Iterator[bytes]: ...
    def geturl(self) -> str | None: ...