import React from "react";

function StatusCard({ status, apiBase }) {
  return (
    <div className="status-card">
      <span className={`status-dot ${status}`}></span>
      <div>
        <strong>
          {status === "connected"
            ? "Backend conectado"
            : status === "offline"
              ? "Backend sin conexión"
              : "Verificando backend"}
        </strong>
        <p>La interfaz consulta el servicio de búsqueda en {apiBase}</p>
      </div>
    </div>
  );
}

export default StatusCard;
