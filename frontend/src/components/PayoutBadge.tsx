const config = {
  cpa: {
    label: "CPA",
    color: "bg-emerald-100 text-emerald-500 border-emerald-300",
  },
  fixed: {
    label: "Fixed",
    color: "bg-blue-100 text-blue-500 border-blue-300",
  },
  cpa_fixed: {
    label: "Hybrid",
    color: "bg-purple-100 text-purple-500 border-purple-300",
  },
};

const PayoutBadge = ({ type }: { type: keyof typeof config }) => {
  const cn = `${config[type].color} border text-sm rounded-md px-3 py-1 ml-3`;
  const label = config[type].label;

  return <div className={cn}>{label}</div>;
};

export default PayoutBadge;
