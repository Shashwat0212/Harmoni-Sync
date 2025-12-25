# Skrillex Live-Set Playlist Embedding Project

## Goal

Build a **sequence-aware music recommendation system** using Skrillex live set tracklists. The system learns a latent embedding space where tracks that appear in similar DJ contexts are close, enabling generation of **probable playlists** given any Skrillex track.

---

## High-Level Idea (NLP Analogy)

* **Corpus** → Collection of Skrillex live set tracklists
* **Sentence** → One live DJ set (ordered)
* **Token / Word** → One track
* **Context window** → Neighboring tracks in the set
* **Model** → Word2Vec (Skip-gram)
* **Embedding space** → Tracks clustered by co-occurrence and sequence context

---

## Data Sources

Potential sources for live-set tracklists:

* DJ set websites (e.g. 1001Tracklists)
* Fan-maintained setlist archives
* YouTube video descriptions of live sets
* Reddit / forum posts with curated tracklists

Each live set should be captured as an **ordered list of track names**.

---

## Dataset Representation

Raw dataset structure:

```json
[
  ["Track A", "Track B", "Track C"],
  ["Track D", "Track A", "Track E"],
  ["Track B", "Track C", "Track F"]
]
```

Key constraints:

* Order must be preserved
* No shuffling of tracks
* Each list represents one coherent DJ performance

---

## Data Cleaning & Canonicalization

Steps:

1. Normalize track names (lowercase, trim whitespace)
2. Resolve duplicates / aliases if needed
3. Count track frequencies across all sets
4. Remove extremely rare tracks (noise threshold, e.g. < 2 occurrences)
5. Rebuild clean sequences

Optional:

* Map tracks to integer IDs (`track2id`, `id2track`) for downstream tasks

---

## Model Choice: Word2Vec (Skip-gram)

**Why Skip-gram?**

* Better representations for rare tracks
* Stronger semantic structure with small-to-medium datasets
* Well-suited for co-occurrence-based learning

Core hyperparameters to tune:

* `vector_size` (e.g. 64–256)
* `window` (context size, e.g. 3–5 tracks)
* `negative` (negative sampling rate)
* `epochs`

---

## Training Objective

Learn embeddings such that:

> Tracks that appear in similar DJ contexts (before/after similar tracks) are close in vector space.

This implicitly captures:

* Energy transitions
* Genre compatibility
* DJ mixing habits

---

## Inference: Playlist Generation

Given a seed track:

1. Retrieve nearest neighbors in embedding space (cosine similarity)
2. Rank candidate tracks by similarity
3. Optionally filter:

   * Already-played tracks
   * Same artist duplicates
4. Sample or sort to form a **probable playlist continuation**

---

## Evaluation (Offline)

Qualitative:

* Nearest-neighbor sanity checks
* Visualization (e.g. PCA / t-SNE of embeddings)

Quantitative (optional):

* Predict held-out tracks from known DJ sets
* Mean reciprocal rank (MRR) or top-k hit rate

---

## Future Extensions

* Position-aware models (track order weighting)
* Transition-based modeling (bigram / Markov layer)
* Replace Word2Vec with:

  * FastText (subword robustness)
  * Transformer encoder for longer context
* Integrate into a local-first RAG or recommendation system

---

## Status

📌 Planning phase only — no implementation started yet.
