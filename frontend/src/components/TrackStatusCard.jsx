import React from "react";

export default function TrackStatusCard({
  name,
  status,
  features,
  sortReason,
  meta,
  onRemove,
}) {
  const isDone = status === "Done";

  return (
    <div
      style={{
        padding: "18px 22px",
        border: "1px solid #ddd",
        borderRadius: "12px",
        marginBottom: "16px",
        backgroundColor: isDone ? "#eaffea" : "#fff",
        boxShadow: "0 4px 10px rgba(0, 0, 0, 0.05)",
        fontFamily: "'Segoe UI', sans-serif",
        fontSize: "15px",
        lineHeight: "1.5",
        position: "relative",
      }}
    >
      {/* Header */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-start",
          marginBottom: "10px",
        }}
      >
        <div style={{ fontWeight: 600, fontSize: "16px", color: "#723480" }}>
          {name}
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
          <span
            style={{
              fontStyle: "italic",
              fontWeight: 500,
              fontSize: "14px",
              color: isDone ? "#808034" : "#999",
            }}
          >
            {status}
          </span>
          <button
            onClick={onRemove}
            title="Remove"
            style={{
              background: "transparent",
              border: "none",
              fontSize: "18px",
              color: "#ccc",
              cursor: "pointer",
              lineHeight: 1,
            }}
          >
            ×
          </button>
        </div>
      </div>

      {/* Features */}
      {features && (
        <div
          style={{
            display: "flex",
            gap: "32px",
            fontSize: "14px",
            color: "#333",
            marginBottom: sortReason ? "8px" : "0",
          }}
        >
          <div>
            <strong style={{ color: "#808034" }}>Tempo:</strong>{" "}
            {features.tempo} BPM
          </div>
          <div>
            <strong style={{ color: "#808034" }}>Key:</strong> {features.key}
          </div>
          <div>
            <strong style={{ color: "#808034" }}>Mood:</strong> {features.mood}
          </div>
        </div>
      )}

      {/* Metadata */}
      {meta && (
        <div
          style={{
            display: "flex",
            gap: "32px",
            fontSize: "13px",
            color: "#555",
            marginTop: "8px",
          }}
        >
          <div>
            <strong>Artist:</strong> {meta.artist}
          </div>
          <div>
            <strong>Genre:</strong> {meta.genre}
          </div>
          <div>
            <strong>Length:</strong> {meta.length}s
          </div>
          <div>
            <strong>Lang:</strong> {meta.language}
          </div>
        </div>
      )}

      {sortReason && (
        <div
          style={{
            fontStyle: "italic",
            color: "#723480",
            fontSize: "13px",
            marginTop: "6px",
          }}
        >
          {sortReason}
        </div>
      )}
    </div>
  );
}
