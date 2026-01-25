import type { PayoutResp } from "../client";
import { HiTrendingUp } from "react-icons/hi";
import { PiCurrencyDollar } from "react-icons/pi";
import { FiZap } from "react-icons/fi";
import Button from "./Button";
import CountryOverrides from "./CountriesAccordion";

const config = {
  cpa: {
    label: "Cost Per Action",
    color: "bg-emerald-100 text-emerald-500",
    icon: <HiTrendingUp />,
  },
  fixed: {
    label: "Fixed",
    color: "Fixed Payout",
    icon: <PiCurrencyDollar />,
  },
  cpa_fixed: {
    label: "CPA + Fixed Bonus",
    color: "bg-purple-100 text-purple-500",
    icon: <FiZap />,
  },
};

const Payout = ({ payout }: { payout: PayoutResp }) => {
  const { label, icon } = config[payout.type];
  const { cpa_amount, fixed_amount, country_overrides } = payout;

  const maxRate = country_overrides?.length
    ? Math.max(...country_overrides.map((o) => o.cpa_amount))
    : cpa_amount!;

  const cpaDisplay =
    maxRate > cpa_amount! ? `$${cpa_amount}-${maxRate}` : `$${cpa_amount}`;

  const renderRates = () => {
    if (payout.type === "cpa") return <span>{cpaDisplay}</span>;
    if (payout.type === "fixed") return <span>${fixed_amount}</span>;
    return (
      <div className="flex gap-1 flex-row md:flex-col xl:flex-row items-baseline">
        <span>{cpaDisplay}</span>
        <span className="text-base text-emerald-400 font-normal">
          + ${fixed_amount} bonus
        </span>
      </div>
    );
  };

  return (
    <section className="py-5 rounded-lg mt-1">
      <div className="flex items-center gap-2 text-xs text-slate-500">
        {icon}
        {label}
      </div>
      <div className="flex justify-between items-center">
        <div className="font-bold text-3xl text-gray-800 mt-2 mr-2 flex items-baseline">
          {renderRates()}
        </div>
        <Button>View Offer</Button>
      </div>
      {payout.country_overrides && (
        <CountryOverrides overrides={payout.country_overrides} />
      )}
    </section>
  );
};

export default Payout;
