import { useState, useEffect } from "react";
import { Api } from "./client";
import type { OfferResp } from "./client";
import Navbar from "./components/Navbar";
import OffersList from "./components/OffersList";

const api = new Api({
  baseUrl: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
});
const INFLUENCER_ID = Number(import.meta.env.VITE_INFLUENCER_ID) || 1;

function App() {
  const [data, setData] = useState<OfferResp[] | null>([]);
  const [influencerName, setInfluencerName] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    async function fetchData() {
      try {
        const [offersResp, influencerResp] = await Promise.all([
          api.api.getOffers({ influencer_id: INFLUENCER_ID }),
          api.api.getInfluencer(INFLUENCER_ID),
        ]);
        setData(offersResp.data);
        setInfluencerName(influencerResp.data.name);
        setLoading(false);
      } catch (error) {
        setLoading(false);
        setError(error as Error);
      }
    }
    fetchData();
  }, []);

  const offers = data?.filter((offer) =>
    offer.title.toLowerCase().includes(searchTerm.toLowerCase()),
  );

  const renderContent = () => {
    if (error)
      return <p className="text-slate-600 text-lg">Error loading offers.</p>;
    if (loading)
      return <p className="text-slate-600 text-lg">Loading offers...</p>;
    if (offers?.length) return <OffersList offers={offers} />;
    return <p className="text-slate-600 text-lg">Nothing found</p>;
  };

  return (
    <div className="bg-slate-50 min-h-screen">
      <Navbar
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        username={influencerName}
      />
      <main className="container mx-auto p-4 flex flex-col justify-center items-center">
        {renderContent()}
      </main>
    </div>
  );
}

export default App;
