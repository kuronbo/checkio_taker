class CheckIOError(Exception):
    """ルート例外"""


class ValueCheckIOError(CheckIOError):
    """CheckIOからでる`ValueError`"""
