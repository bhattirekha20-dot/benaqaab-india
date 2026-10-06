# Central Private Vault & AI Skills Repository

This is the centralized private repository for custom AI bot skills, private workflows, automation scripts, and reference projects.

---

## 📁 Repository Structure

```text
├── skills/           # AI bot skills, prompt templates, and custom behaviors
├── workflows/        # Automation scripts, tools, and execution pipelines
├── configs/          # Custom configurations and settings templates
├── docs/             # Private notes, design specs, and documentation
├── projects/         # Individual sub-projects and private codebases
├── .gitignore        # Guardrails against leaking tokens, .env, and local temp files
└── README.md         # Repository documentation
```

---

## 🔒 Security Best Practices

1. **Never commit raw credentials**: Store all API tokens, keys, and passwords in `.env` files (which are ignored by default).
2. **Use environment variables**: Always read secrets from system environments or secure key vaults.
3. **Keep remote private**: Ensure GitHub/GitLab repository visibility is strictly set to **Private**.
