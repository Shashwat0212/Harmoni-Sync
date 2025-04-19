import React from "react";

export default function PlaylistPreview({ files }) {
  return (
    <div>
      <h3>Playlist Preview:</h3>
      <ul>
        {files.map((file, index) => (
          <li key={index}>{file.name}</li>
        ))}
      </ul>
    </div>
  );
}
