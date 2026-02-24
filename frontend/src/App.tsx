import { useState, useEffect } from "react";
import { Api } from "./client";
import type { OfferResp } from "./client";
import Navbar from "./components/Navbar";
import OffersList from "./components/OffersList";

const api = new Api({
  baseUrl: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
});

function parseUrl(): number | null {
  const params = new URLSearchParams(window.location.search);
  const id = params.get("influencer_id");
  return id ? Number(id) : null;
}

function App() {
  const [data, setData] = useState<OfferResp[] | null>([]);
  const [influencerName, setInfluencerName] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<unknown>(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [influencerId] = useState<number | null>(parseUrl);

  useEffect(() => {
    async function fetchData() {
      try {
        const offersResp = await api.api.getOffers(
          influencerId ? { influencer_id: influencerId } : {},
        );
        setData(offersResp.data);

        if (influencerId) {
          const influencerResp = await api.api.getInfluencer(influencerId);
          setInfluencerName(influencerResp.data.name);
        }
        setLoading(false);
      } catch (error) {
        setLoading(false);
        setError(error as Error);
      }
    }
    fetchData();
  }, [influencerId]);

  const offers = data?.filter((offer) =>
    offer.title.toLowerCase().includes(searchTerm.toLowerCase()),
  );

  const renderContent = () => {
    if (error) {
      const msg =
        error instanceof Response && error.status === 404 && influencerId
          ? `Influencer with ID ${influencerId} not found.`
          : "Error loading offers.";
      return <p className="text-slate-600 text-lg">{msg}</p>;
    }
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
        loading={loading}
      />
      <main className="container mx-auto p-4">{renderContent()}</main>
    </div>
  );
}

export default App;
