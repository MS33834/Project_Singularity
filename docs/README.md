# Project Singularity — GitHub Pages

This directory contains the source for the Project Singularity introduction site.

## Live site

After enabling GitHub Pages, the site will be available at:

```
https://ms33834.github.io/Project_Singularity/
```

## Enabling Pages

1. Go to **Settings → Pages** in the GitHub repository.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Choose the `main` branch and the `/docs` folder.
4. Save. The site will build in about one minute.

## Local preview

You can preview the site locally without any build step:

```bash
cd docs
python -m http.server 8000
```

Then open http://localhost:8000.

## Files

- `index.html` — main page
- `assets/style.css` — theme and layout
- `assets/script.js` — language switcher (English / 中文)

## Design notes

- Dark theme with teal and orange accents, matching the Project Singularity visual identity.
- English-first content with a Chinese switcher.
- No heavy animations or generic AI buzzwords; focused on workflow, tools, and repositories.
