import React from "react";

export default function ArtistStyleSelector({ selectedStyle, onChange }) {
  const handleChange = (e) => {
    onChange(e.target.value);
  };

  return (
    <select
      value={selectedStyle}
      onChange={handleChange}
      style={{
        padding: "10px 12px",
        border: "1px solid #723480", // plum border
        borderRadius: "8px",
        backgroundColor: "#DBD4FF", // soft lavender
        color: "#333",
        fontSize: "14px",
        width: "100%",
        cursor: "pointer",
        outline: "none",
        boxShadow: "0 2px 6px rgba(114, 52, 128, 0.15)", // subtle plum shadow
        transition: "border 0.3s ease",
      }}
      onFocus={(e) => (e.target.style.border = "1px solid #808034")}
      onBlur={(e) => (e.target.style.border = "1px solid #723480")}
    >
      <option value="">Select...</option>
      <option value="Hardwell">Hardwell pre-2020</option>
      <option value="MartinGarrix">Martin Garrix</option>
      <option value="Armin">Armin van Buuren</option>
    </select>
  );
}
