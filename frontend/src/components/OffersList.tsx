import { motion } from "motion/react";
import OfferCard from "./OfferCard";
import type { OfferResp } from "../client";

const OffersList = ({ offers }: { offers: OfferResp[] }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">
      {offers?.map((offer, index) => (
        <motion.div
          key={offer.id}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.1 }}
        >
          <OfferCard offer={offer} />
        </motion.div>
      ))}
    </div>
  );
};

export default OffersList;
