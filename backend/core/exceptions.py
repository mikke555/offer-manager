from fastapi import HTTPException, status


class AppException(HTTPException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "An error occurred"

    def __init__(self, **format_args):
        detail = self.detail.format(**format_args) if format_args else self.detail
        super().__init__(status_code=self.status_code, detail=detail)


class NotFoundException(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "{name} with id {id} not found"


class OfferNotFoundException(NotFoundException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Offer with id {id} not found"


class InfluencerNotFoundException(NotFoundException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Influencer with id {id} not found"


class PayoutAlreadyExistsException(AppException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Payout for offer {offer_id} and given influencer already exists"


class InvalidCategoryException(AppException):
    status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
    detail = "This category is not allowed"


class DefaultPayoutDeletionException(AppException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Cannot delete the default payout"
