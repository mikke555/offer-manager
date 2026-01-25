import { useState } from "react";
import { FiChevronDown } from "react-icons/fi";
import type { CountryOverrideResp } from "../client";
import { CiGlobe } from "react-icons/ci";
import { AnimatePresence, motion } from "motion/react";

interface CountryOverridesProps {
  overrides: CountryOverrideResp[];
}

const CountryOverrides = ({ overrides }: CountryOverridesProps) => {
  const [isExpanded, setIsExpanded] = useState(false);

  if (overrides.length === 0) return null;

  return (
    <div className="mt-3 pt-4">
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="
          flex items-center gap-1 
          text-xs text-slate-500 hover:text-slate-700
          transition-colors cursor-pointer
        "
      >
        <CiGlobe /> Country-specific rates ({overrides.length})
        <span
          className={`transition-transform ${isExpanded ? "rotate-180" : ""}`}
        >
          <FiChevronDown />
        </span>
      </button>
      <AnimatePresence>
        {isExpanded && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2, ease: "easeOut" }}
            className="overflow-hidden"
          >
            <div className="flex flex-wrap gap-2 mt-3">
              {overrides.map((override) => (
                <div
                  key={override.id}
                  className="
                  items-center gap-1.5 rounded-full px-2.5 py-1
                  font-medium text-slate-700 bg-slate-100 text-sm
                  "
                >
                  {override.country_code} ${override.cpa_amount}
                </div>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default CountryOverrides;
