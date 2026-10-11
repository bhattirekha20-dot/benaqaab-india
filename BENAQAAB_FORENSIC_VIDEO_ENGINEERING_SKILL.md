# 🛠️ BENAQAAB FORENSIC VIDEO ENGINEERING SKILL (v2.0)

> **AUTHORITY:** This is the supreme, unified Video Engineering Skill for Benaqaab India, forged from the exhaustive forensic analysis of 11,121 world-class masterclass frames.
> **PURPOSE:** To completely eradicate "AI Slop" and generate high-retention, hyper-causal documentary videos where every pixel is enslaved to the voiceover audio.

---

## 🧠 CORE PHILOSOPHY: THE CAUSAL LOCKSTEP
You are no longer "adding footage to a voiceover." You are building a **Kinetic Audio-Visual Engine**. 
Every visual event (cut, zoom, color shift) must be a direct, physical reaction to a specific spoken word. If a visual is not anchored to a word, it is filler and must be deleted.

---

## 📐 THE 5 LAWS OF FORENSIC EDITING

### LAW 1: THE "IMPACT WORD" TRIGGER
Never transition a visual *before* or *after* the core subject of the sentence. 
*   **The Rule:** Identify the highest-impact word in a sentence (e.g., *Size, Scam, Crore, Exposed, Secret*). The visual must explode, cut, or deploy a callout pin on the exact millisecond the first syllable of that word is spoken.
*   **Execution:** In `comp.html`, map your GSAP triggers directly to the `word_timestamps` array of the TTS engine.

### LAW 2: THE "BUT" COLOR PIVOT (Contradiction Inversion)
*   **The Rule:** Whenever the script introduces a contradiction or dark truth (using words like *But, However, लेकिन, सच्चाई*), the video must execute a `HARD_SCENE_CUT` that instantly flips the color palette.
*   **Execution:** Transition from safe/warm colors (Cyan/Gold) to forensic danger colors (Crimson Flame `#F43F5E` or Signal Amber `#FBBF24`). Do not ease this transition; cut it violently to wake up the viewer's brain.

### LAW 3: THE HYPER-CUT TIME COMPRESSION
*   **The Rule:** Visual cut-rate is mathematically proportional to the audio's temporal scope. If the audio describes a long timeframe (e.g., "100 years of history" or "a massive global network"), do not use one long panning shot.
*   **Execution:** Execute a **3-Frame Flash Cut** (3 consecutive archival images flashing rapidly, 1 per second). Rapid visual firing forces the brain to process "massive scale" instantly.

### LAW 4: THE SCIENTIFIC LOCKDOWN (Micro-Drift)
*   **The Rule:** When the narrator shifts from storytelling to explaining hard science, math, or forensic proof, the rapid editing must stop.
*   **Execution:** Lock the camera into a `STATIC_OR_MICRO_DRIFT`. Dim the background (`backdrop-filter: blur(16px)`). A static camera signals to the subconscious: "Stop watching the colors, read this evidence. This is the absolute truth."

### LAW 5: THE ROLLING FORENSIC PRIMITIVES
Static text is strictly forbidden. 
*   **The Rule:** Every piece of evidence must be physically interacted with by the rendering engine.
*   **Execution:** 
    1.  **Odometers:** If a number is spoken, a tabular monospace odometer (`JetBrains Mono`) must roll up from 0 to the target number, decelerating using `cubic-bezier(0.16, 1, 0.3, 1)`.
    2.  **The Authentic Highlighter:** If a document is quoted, an organic yellow highlighter (`globalCompositeOperation = 'multiply'`, hex `#FFE600`) must draw over the text in real-time with the voiceover.
    3.  **The 2.5x Loupe:** If a small detail is critical, a specular glass loupe must physically zoom into the frame precisely when the detail is spoken.

---

## ⚙️ RENDER TARGET REQUIREMENTS (`comp.html`)
When generating the final video composition file, you must adhere to these technical standards extracted from the 11,121-frame database:
1.  **Average Shot Length (ASL):** Maintain a structural progression every ~4.2 seconds.
2.  **Canvas Isolation:** Zero HTML preview chrome allowed (`.render-mode` must hide all controls).
3.  **The Descent Gradient:** Use ambient volumetric lighting in the background that shifts based on the narrative tone (e.g., bright surface cyan transitioning to crushing black as the topic gets darker).
4.  **Absolute Time Contract:** Implement `window.seek(t)`. Every cut, highlighter sweep, and odometer roll must be perfectly deterministic and reproducible when seeking to timestamp $t$.

> **MANDATE:** Read and apply this skill before writing a single line of script or code for Benaqaab India videos. This is the only acceptable standard.
