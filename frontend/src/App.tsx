import { useState, useEffect } from "react";
import { Api } from "./client";
import type { OfferResp } from "./client";
import Navbar from "./components/Navbar";
import OffersList from "./components/OffersList";

const api = new Api({ baseUrl: "http://127.0.0.1:8000" });

function App() {
  const [data, setData] = useState<OfferResp[] | null>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    async function fetchData() {
      try {
        const resp = await api.api.getOffers();
        setData(resp.data);
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
      <Navbar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      <main className="container mx-auto p-4 flex flex-col justify-center items-center">
        {renderContent()}
      </main>
    </div>
  );
}

export default App;
