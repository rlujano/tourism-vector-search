import React from "react";

function SearchForm({ query, onQueryChange, onSubmit, loading }) {
  return (
    <form className="search-form" onSubmit={onSubmit}>
      <input
        type="text"
        value={query}
        onChange={(event) => onQueryChange(event.target.value)}
        placeholder="Ej. lugares mágicos"
        aria-label="Consulta de búsqueda"
      />
      <button type="submit" disabled={loading}>
        {loading ? "Buscando..." : "Buscar"}
      </button>
    </form>
  );
}

export default SearchForm;
