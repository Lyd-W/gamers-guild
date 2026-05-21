from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    default_acl = "public-read"
    object_parameters = {
        "CacheControl": "max-age=31536000, public, immutable",
    }


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    default_acl = "public-read"
    object_parameters = {
        "CacheControl": "max-age=86400, public",
    }