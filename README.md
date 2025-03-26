# 🎵 HarmoniSync - Intelligent Track Sequencer

**HarmoniSync** is a modular full-stack music analysis and sequencing platform designed for DJs and music enthusiasts to create **mood-aware, harmonically compatible** playlists. It intelligently analyzes audio features like **key, BPM, energy, mood, and genre**, and arranges tracks in an optimal order using the **Camelot Wheel** and artist-style sorting presets.

---

## 🚀 Features

### 🎼 **Track Analysis**
- Extracts **key**, **tempo (BPM)**, **energy**, **timbre**, **pitch**, **intensity**, and **duration**.
- Analyzes **language** and **lyrics** using **Whisper ASR** and **YAMNet** for vocal detection.
- Applies **transformer-based sentiment analysis** on lyrics to detect emotional tone.
- Assigns mood using **Thayer’s Mood Model** via DSP feature mapping.

### 🧠 **Cultural & Artist-Aware Mood Classification**
- Modular **region-based mood engines** (starting with an India-centric model).
- Balances **lyric sentiment**, **musical features**, and **artist-style presets** to assign mood.
- Early stopping in transcription for performance efficiency.

### 🔀 **Smart Sequencing**
- Sorts tracks using **Camelot Wheel** for harmonic compatibility.
- Prioritizes **mood, BPM, and artist style** to optimize playlist flow.
- Prevents clashing tempos or contradictory transitions.

### 🔊 **Beatmatching & Mixing Optimization**
- Ensures smooth transitions by aligning **beats and harmonic keys**.
- Automates track progression for a seamless DJ set or personal listening experience.

---

## 💻 Frontend UI (ReactJS)

- Built with **ReactJS**, **TailwindCSS**, and **shadcn/ui** for a clean, modern design.
- 🎧 **Drag-and-Drop Section**: Upload multiple songs effortlessly.
- 🎶 **Current Playlist Preview**: Displays uploaded songs and allows removal.
- 📊 **Sorting Animation** (coming soon): Visualizes intelligent track reordering.
- 🎛️ **Artist Style Selector**: Choose an artist-style (e.g. “Hardwell pre-2020”) to influence sorting.
- 🔈 **Integrated Audio Player**: Play sorted tracks with mood-based crowd reactions like:
  - *“Now the crowd goes crazy!”*
  - *“Let’s cool things down…”*

---

## 🔮 Future Enhancements

- **DJ Software Integration**: Rekordbox, Serato, Virtual DJ
- **AI Track Recommendations**: Personalized song suggestions based on mood and style
- **Live Suggestions & Real-Time Feedback** during mixing
- **Multiple Regional Mood Engines** for cultural expansion (e.g., US, Japan)

---

## 🛠️ Tech Stack

- **Frontend**: ReactJS, TailwindCSS, shadcn/ui
- **Backend**: Spring Boot (Java)
- **Analyzer**: Python (Flask, Whisper, YAMNet, librosa, Transformers)
- **Architecture**: Microservices with modular analyzers and pluggable mood engines

---

## 📬 Contact

👤 **Shashwat Srivastava**  
🔗 [LinkedIn](https://www.linkedin.com/in/shashwat-srivastava-858466202/)
