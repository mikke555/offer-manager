import type { OfferResp } from "../client";
import CategoryList from "./CategoryList";
import Payout from "./Payout";
import PayoutBadge from "./PayoutBadge";

const OfferCard = ({ offer }: { offer: OfferResp }) => {
  return (
    <div
      className="
        bg-white py-4 px-5 rounded-xl  
        transition-all duration-300
        shadow-lg hover:shadow-xl 
        hover:-translate-y-1 
        border border-transparent hover:border-emerald-100
      "
    >
      <div className="flex justify-between gap-1">
        <h3 className="font-bold text-gray-800 tracking-wide truncate text-xl">
          {offer.title}
        </h3>
        <PayoutBadge type={offer.payout.type} />
      </div>
      <p className="text-sm text-slate-500 mt-2">{offer.description}</p>
      {offer.categories && <CategoryList categories={offer.categories} />}
      <Payout payout={offer.payout} />
    </div>
  );
};

export default OfferCard;
