import React from "react";

function ResultList({ results }) {
  if (!results.length) return null;

  return (
    <div className="results-grid">
      {results.map((item) => (
        <article key={item.id} className="result-card">
          <div className="result-top">
            <span className="pill">{item.category || "Atractivo"}</span>
            <span className="score">Score {item.score}</span>
          </div>
          <h3>{item.name}</h3>
          <p>{item.description}</p>
          <div className="meta">
            <span>📍 {item.location}</span>
          </div>
        </article>
      ))}
    </div>
  );
}

export default ResultList;
