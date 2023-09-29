from urllib.parse import urlparse
from fastapi import HTTPException


def validate_url_format(url):
        try:
            parsed_url = urlparse(url)
            # Check if the scheme is valid
            if parsed_url.scheme not in ("http", "https"):
                raise HTTPException(status_code=422, detail={'error': "URL must have a valid scheme (http/https)"})
            # Check if the domain contains a dot (.)
            if "." not in parsed_url.netloc:
                raise HTTPException(status_code=422, detail={'error': "Invalid URL format: missing dot in domain"})
        except ValueError as e:
            raise HTTPException(status_code=422, detail={'error': "Invalid URL format"}) from e
