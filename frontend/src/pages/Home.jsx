import React, { useState } from "react";
import axios from "axios";
import FileUploader from "../components/FileUploader";
import ArtistStyleSelector from "../components/ArtistStyleSelector";
import TrackStatusCard from "../components/TrackStatusCard";

export default function Home() {
  const [files, setFiles] = useState([]);
  const [artistStyle, setArtistStyle] = useState("");

  const handleFilesSelected = async (selectedFiles) => {
    const formData = new FormData();
    selectedFiles.forEach((file) => {
      formData.append("files", file);
    });

    try {
      const response = await axios.post(
        "http://localhost:8080/api/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      const trackList = response.data;

      const enrichedFiles = trackList.map((track) => ({
        name: track.title,
        status: "Done",
        features: {
          tempo: track.bpm,
          key: track.key,
          mood: track.mood,
        },
        sortReason: null,
        meta: {
          artist: track.artist,
          genre: track.genre,
          length: track.length,
          language: track.language,
        },
      }));

      setFiles((prev) => [...prev, ...enrichedFiles]);
    } catch (error) {
      console.error("Upload failed:", error);
      alert("Failed to analyze tracks. Please try again.");
    }
  };

  const handleRemoveFile = (name) => {
    setFiles((prev) => prev.filter((file) => file.name !== name));
  };

  const allDone =
    files.length > 0 && files.every((file) => file.status === "Done");

  const sortAndAnnotateTracks = () => {
    const sorted = [...files].sort(
      (a, b) => a.features.tempo - b.features.tempo
    );

    const updated = sorted.map((track, index) => {
      let reason = "";
      if (index === 0) reason = "🎧 Starting smooth";
      else {
        const diff = track.features.tempo - sorted[index - 1].features.tempo;
        reason = diff > 0 ? "⚡ We build energy" : "🌙 We slow down a little";
      }
      return { ...track, sortReason: reason };
    });

    setFiles(updated);
  };

  return (
    <div
      style={{
        maxWidth: "760px",
        margin: "40px auto",
        padding: "36px",
        backgroundColor: "#FFFFE3",
        borderRadius: "16px",
        boxShadow: "0 8px 20px rgba(0, 0, 0, 0.08)",
        fontFamily: "'Segoe UI', sans-serif",
        color: "#333",
        border: "1px solid #EAEAEA",
      }}
    >
      <h1
        style={{
          fontSize: "26px",
          fontWeight: 700,
          marginBottom: "24px",
          display: "flex",
          alignItems: "center",
          gap: "10px",
          color: "#723480",
        }}
      >
        🎵 <span>HarmoniSync:</span>{" "}
        <span style={{ fontWeight: 400, color: "#808034" }}>
          Intelligent Track Sequencer
        </span>
      </h1>

      <div style={{ marginBottom: "20px" }}>
        <label
          style={{ fontWeight: 600, marginBottom: "6px", fontSize: "14px" }}
        >
          Upload your tracks:
        </label>
        <FileUploader onFilesSelected={handleFilesSelected} />
      </div>

      <div style={{ marginBottom: "30px" }}>
        <label
          style={{ fontWeight: 600, marginBottom: "6px", fontSize: "14px" }}
        >
          Choose Artist Style:
        </label>
        <ArtistStyleSelector
          selectedStyle={artistStyle}
          onChange={setArtistStyle}
        />
      </div>

      <h3
        style={{
          marginBottom: "16px",
          fontSize: "18px",
          fontWeight: 600,
          color: "#723480",
        }}
      >
        Playlist Preview:
      </h3>

      {files.map((file) => (
        <TrackStatusCard
          key={file.name}
          name={file.name}
          status={file.status}
          features={file.features}
          sortReason={file.sortReason}
          meta={file.meta}
          onRemove={() => handleRemoveFile(file.name)}
        />
      ))}

      {allDone && (
        <button
          onClick={sortAndAnnotateTracks}
          style={{
            marginTop: "20px",
            padding: "10px 18px",
            fontSize: "14px",
            fontWeight: 600,
            backgroundColor: "#808034",
            color: "#fff",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            display: "flex",
            alignItems: "center",
            gap: "8px",
            transition: "background-color 0.3s ease",
          }}
          onMouseOver={(e) => (e.target.style.backgroundColor = "#6b692b")}
          onMouseOut={(e) => (e.target.style.backgroundColor = "#808034")}
        >
          🔀 Sort Playlist
        </button>
      )}
    </div>
  );
}
