import { useState, useEffect } from "react";
import { Api } from "./client";
import type { OfferResp } from "./client";

const api = new Api({ baseUrl: "http://127.0.0.1:8000" });

function App() {
  const [data, setData] = useState<OfferResp[] | null>(null);

  useEffect(() => {
    async function fetchData() {
      const resp = await api.api.getOffers();
      setData(resp.data);
    }
    fetchData();
  }, []);

  return (
    <>
      <div>{data?.map((offer) => offer.title)}</div>
    </>
  );
}

export default App;
