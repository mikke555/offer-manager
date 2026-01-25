import OfferCard from "./OfferCard";
import type { OfferResp } from "../client";

const OffersList = ({ offers }: { offers: OfferResp[] }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">
      {offers?.map((offer) => (
        <OfferCard key={offer.id} offer={offer} />
      ))}
    </div>
  );
};

export default OffersList;
