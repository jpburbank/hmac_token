from typing import Any, Dict, List, Iterable
import hmac
from hashlib import sha1
from hmac import HMAC


CHAR_ENCODING = "utf-8"
secret = "this is a secret key that should be moved to secrets file"
secret_key = secret.encode(encoding=CHAR_ENCODING)

def generate_digest(request: Dict[str, Any]) -> str:
    digest_creator = hmac.new(secret_key, digestmod=sha1)
    add_to_digest(digest_creator, request.items())
    return digest_creator.hexdigest()

def add_to_digest(digest_creator: HMAC, pairs: Iterable[Any]) -> None:
    for key, value in pairs:
        update(digest_creator, key)
        if isinstance(value, dict):
            add_to_digest(digest_creator, value.items())
        elif isinstance(value, list):
            add_to_digest(digest_creator, enumerate(value))
        else:
            update(digest_creator, value)

def update(digest_creator: HMAC, value: Any) -> None:
    digest_creator.update(
        (str(value) if not isinstance(value, str) else value).encode(encoding=CHAR_ENCODING)
    )