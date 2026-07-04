import React from "react";

const FALLBACK_IMAGE =
  "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80";

function ResultList({ results }) {
  if (!results.length) return null;

  return (
    <div className="results-grid gap-6 md:grid-cols-2 xl:grid-cols-3">
      {results.map((item) => {
        const imageUrl = item.image_url || FALLBACK_IMAGE;

        return (
          <article key={item.id} className="result-card">
            <img
              src={imageUrl}
              alt={item.name}
              onError={(event) => {
                event.currentTarget.src = FALLBACK_IMAGE;
              }}
            />

            <div className="result-card-content">
              <div className="result-top">
                <span className="pill">{item.category || "Atractivo"}</span>
                <span className="score">Score {item.score}</span>
              </div>

              <h3>{item.name}</h3>
              <p>{item.description}</p>

              <div className="meta">
                <span>📍 {item.location}</span>
              </div>
            </div>
          </article>
        );
      })}
    </div>
  );
}

export default ResultList;
