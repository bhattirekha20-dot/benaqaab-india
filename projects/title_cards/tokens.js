/**
 * tokens.js — Design tokens, timing specifications, and line data
 * Deterministic Canvas2D Title Card Video Engine
 */

export const W = 1920;
export const H = 1080;
export const FPS = 30;
export const MARGIN = 144;

export const PALETTE = {
  background: '#0b0b0f',
  ink: '#f4f2ec',
  accent: '#c8ff3d'
};

export const FONT = {
  family: 'Space Grotesk',
  weight: 700,
  size: 168,
  file: 'fonts/SpaceGrotesk-Bold.woff2'
};

export const TIMING = {
  fadeIn: 0.5,       // seconds to fade in while rising
  fadeOut: 0.25,     // seconds to fade out
  risePx: 40,        // rise distance in px
  headPause: 0.35,   // subtle initial clean slate before first card
  tailPause: 0.65,   // clean hold at end before loop/cut
  // Formula scale factor to achieve target 15-20s video:
  // Base formula: max(1.2, 0.35 + words/3.2)
  holdScale: 1.65    // Scaled so 5 default cards total ~16.0s
};

/**
 * Default input lines: 1 to 6 words each.
 * Exactly one word per card receives the accent colour.
 */
export const LINES = [
  { text: "Every frame is code", accent: "code" },
  { text: "Nothing is filmed", accent: "filmed" },
  { text: "Same input", accent: "input" },
  { text: "Same pixels", accent: "pixels" },
  { text: "Render it free", accent: "free" }
];

/**
 * Helper to compute the exact timeline of cards.
 * Returns array of card schedule descriptors and total duration.
 */
export function buildTimeline(lines = LINES, timing = TIMING) {
  let currentTime = timing.headPause;

  const cards = lines.map((line, index) => {
    const words = line.text.trim().split(/\s+/);
    const rawHold = Math.max(1.2, 0.35 + (words.length / 3.2));
    const holdDuration = rawHold * (timing.holdScale || 1.0);
    const cardDuration = timing.fadeIn + holdDuration + timing.fadeOut;

    const schedule = {
      index,
      text: line.text,
      accent: line.accent,
      words,
      startTime: currentTime,
      fadeInEnd: currentTime + timing.fadeIn,
      holdEnd: currentTime + timing.fadeIn + holdDuration,
      endTime: currentTime + cardDuration,
      duration: cardDuration,
      holdDuration
    };

    currentTime += cardDuration;
    return schedule;
  });

  const totalDuration = currentTime + timing.tailPause;

  return {
    cards,
    duration: parseFloat(totalDuration.toFixed(3))
  };
}
