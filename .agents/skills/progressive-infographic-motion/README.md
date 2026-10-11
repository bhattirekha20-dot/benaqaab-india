# Progressive Infographic Motion Skill

## Install for an AI agent

Copy the entire folder below into the AI agent's skills directory:

```text
skills/progressive-infographic-motion/
├── SKILL.md
├── README.md
├── references/
│   ├── editing-capabilities.md
│   └── demographic-clock-conversation-map.md
└── templates/
    ├── editor-handoff-template.md
    └── motion-manifest-template.json
```

The AI should load/read `SKILL.md` before creating a motion graphic, animated dashboard, motion-reference HTML file, or a video-editor storyboard from static images.

## Use with this project

Use the generated file below as the working example/reference:

```text
/home/user/demographic-clock-motion-reference.html
```

Its machine-readable motion plan is exposed in the browser as:

```js
window.MOTION_REFERENCE
```

The skill deliberately uses **relative phases only**. The AI/video editor decides the final video duration, pacing, and FPS.
