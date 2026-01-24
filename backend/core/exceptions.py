from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    noun = "Resource"

    def __init__(self, id: int | None = None):
        detail = (
            f"{self.noun} with id {id} not found"
            if id is not None
            else f"{self.noun} not found"
        )
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class OfferNotFoundException(NotFoundException):
    noun = "Offer"


class InfluencerNotFoundException(NotFoundException):
    noun = "Influencer"


class CustomPayoutNotFoundException(NotFoundException):
    noun = "Custom payout"


class InvalidCategoryException(HTTPException):
    def __init__(self, detail: str = "This category is not allowed"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=detail
        )


class CustomPayoutAlreadyExistsException(HTTPException):
    def __init__(self, offer_id: int, influencer_id: int):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Custom payout for offer {offer_id} and influencer {influencer_id} already exists",
        )
