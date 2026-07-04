const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function checkBackendHealth() {
  const response = await fetch(`${API_BASE}/health`);
  if (!response.ok) throw new Error("Backend no disponible");

  const data = await response.json();
  return data?.status === "ok" ? "connected" : "warning";
}

export async function searchAttractions(query) {
  const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
  if (!response.ok) throw new Error("No fue posible completar la búsqueda.");

  const data = await response.json();
  return data.results || [];
}

export { API_BASE };
