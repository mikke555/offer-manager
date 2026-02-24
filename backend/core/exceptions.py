from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, id: int | None = None, name: str | None = "Resource"):
        self.id = id
        self.name = name

        detail = (
            f"{self.name} with id {self.id} not found"
            if id is not None
            else f"{self.name} not found"
        )
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class OfferNotFoundException(NotFoundException):
    def __init__(self, id: int | None = None):
        super().__init__(id=id, name="Offer")


class InfluencerNotFoundException(NotFoundException):
    def __init__(self, id: int | None = None):
        super().__init__(id=id, name="Influencer")


class PayoutAlreadyExistsException(HTTPException):
    def __init__(self, offer_id: int, influencer_id: int | None):
        target = f"influencer {influencer_id}" if influencer_id else "default"
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Payout for offer {offer_id} ({target}) already exists",
        )


class InvalidCategoryException(HTTPException):
    def __init__(self, detail: str = "This category is not allowed"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=detail
        )
