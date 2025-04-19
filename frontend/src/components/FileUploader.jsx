import React from "react";

export default function FileUploader({ onFilesSelected }) {
  const handleFileChange = (e) => {
    const files = Array.from(e.target.files);
    onFilesSelected(files);
  };

  return (
    <input
      type="file"
      accept="audio/*"
      multiple
      onChange={handleFileChange}
      style={{
        padding: "8px 12px",
        border: "2px dashed #DBD4FF", // pastel lavender border
        borderRadius: "10px",
        backgroundColor: "#fff",
        fontSize: "14px",
        color: "#333",
        width: "100%",
        cursor: "pointer",
        transition: "border-color 0.3s ease",
      }}
      onMouseOver={
        (e) => (e.target.style.borderColor = "#723480") // plum hover
      }
      onMouseOut={(e) => (e.target.style.borderColor = "#DBD4FF")}
      title="Select audio files to analyze"
    />
  );
}
