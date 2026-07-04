import React, { useEffect, useState } from "react";
import SearchForm from "./components/SearchForm";
import ResultList from "./components/ResultList";
import StatusCard from "./components/StatusCard";
import { API_BASE, checkBackendHealth, searchAttractions } from "./services/api";

const SAMPLE_QUERIES = [
  "lugares mágicos de Puno",
  "playas en Lima",
  "museos en Cusco",
  "rutas en Arequipa",
];

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [status, setStatus] = useState("checking");

  useEffect(() => {
    const verifyHealth = async () => {
      try {
        const nextStatus = await checkBackendHealth();
        setStatus(nextStatus);
      } catch {
        setStatus("offline");
      }
    };

    verifyHealth();
  }, []);

  const handleSearch = async (event) => {
    event.preventDefault();
    const trimmedQuery = query.trim();

    if (!trimmedQuery) {
      setError("Escribe una consulta para buscar atractivos turísticos.");
      return;
    }

    setLoading(true);
    setError("");
    setResults([]);

    try {
      const nextResults = await searchAttractions(trimmedQuery);
      setResults(nextResults);

      if (!nextResults.length) {
        setError("No se encontraron resultados para esa búsqueda.");
      }
    } catch (err) {
      setError(err.message || "Ocurrió un error al consultar el backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <header className="hero">
        <div className="hero-copy">
          <p className="eyebrow">Tourism Vector Search</p>
          <h1>Descubre destinos con búsquedas inteligentes</h1>
          <p className="hero-text">
            Busca atractivos turísticos por significado, contexto y ubicación con el motor de búsqueda semántico del proyecto.
          </p>

          <SearchForm query={query} onQueryChange={setQuery} onSubmit={handleSearch} loading={loading} />

          <div className="suggestions">
            {SAMPLE_QUERIES.map((item) => (
              <button key={item} type="button" onClick={() => setQuery(item)}>
                {item}
              </button>
            ))}
          </div>
        </div>

        <StatusCard status={status} apiBase={API_BASE} />
      </header>

      <main className="results-section">
        {error ? <p className="message error">{error}</p> : null}

        {!loading && !error && !results.length ? (
          <div className="empty-state">
            <h2>Prueba una búsqueda</h2>
            <p>Escribe un término como “playas”, “museos” o una región para empezar.</p>
          </div>
        ) : null}

        <ResultList results={results} />
      </main>
    </div>
  );
}

export default App;
