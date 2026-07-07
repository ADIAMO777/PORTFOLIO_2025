# ADIAMO BANKOLE — Frontend Developer Portfolio

Personal portfolio showcasing projects, skills, and services. Built with HTML, CSS, and JavaScript — no framework — deployed on Vercel.

**Live site:** [portfolio-2025-five-silk.vercel.app](https://portfolio-2025-five-silk.vercel.app)

## About

I'm **ADIAMO BANKOLE**, a frontend developer based in Nigeria, open to work (remote and on-site). I build responsive, modern, and interactive web experiences with clean code and attention to detail.

## Features

- Responsive layout with mobile navigation
- Scroll animations, typing effect, and project filters
- 11-category skills section (frontend, backend, databases, tools, soft skills, and more)
- Services, projects, testimonials, and blog sections
- Contact form via [Formspree](https://formspree.io)
- Dark mode toggle
- Downloadable CV (PDF)
- SEO meta tags, Open Graph preview, `sitemap.xml`, and `robots.txt`
- Custom 404 page and Vercel Analytics hook

## Projects

| Project | Live Demo | Code |
|---------|-----------|------|
| SwiftCore Solutions | [swift-core-service.netlify.app](https://swift-core-service.netlify.app/) | [GitHub](https://github.com/ADIAMO777/SWIFT-CORE-ORIGINAL) |
| La Bella-Bites | [la-bella-bites.vercel.app](https://la-bella-bites.vercel.app/) | [GitHub](https://github.com/ADIAMO777/LA-BELLA-BITES) |
| Responsive Nav-Bar | [assignment-01-five-chi.vercel.app](https://assignment-01-five-chi.vercel.app/) | [GitHub](https://github.com/ADIAMO777/Assignment-01) |
| Web App UI | [exercise-class.netlify.app](https://exercise-class.netlify.app/) | [GitHub](https://github.com/ADIAMO777/Exercise-01) |

## Tech Stack

- **Markup & styling:** HTML5, CSS3 (custom properties, Grid, Flexbox, animations)
- **Scripting:** Vanilla JavaScript (Intersection Observer, localStorage, Formspree)
- **Fonts:** Google Fonts (Poppins)
- **Deployment:** Vercel
- **Assets:** SVG favicon, project screenshots, generated CV PDF

## Project Structure

```
PORTFOLIO_2025/
├── index.html          # Main portfolio page
├── style.css           # Styles and dark mode
├── script.js           # Interactivity and animations
├── 404.html            # Custom not-found page
├── vercel.json         # Vercel routing config
├── sitemap.xml         # SEO sitemap
├── robots.txt          # Crawler rules
└── assets/
    ├── profile.jpg
    ├── favicon.svg
    ├── og-preview.png
    ├── ADIAMO-BANKOLE-CV.pdf
    ├── generate-cv.py
    └── projects/       # Project screenshots
```

## Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/ADIAMO777/PORTFOLIO_2025.git
   cd PORTFOLIO_2025
   ```
2. Open `index.html` in your browser, or use a local server (e.g. Live Server in VS Code).

No build step or dependencies required to view the site.

## Regenerate CV PDF

Requires Python 3 and [fpdf2](https://pypi.org/project/fpdf2/):

```bash
pip install fpdf2
python assets/generate-cv.py
```

Output: `assets/ADIAMO-BANKOLE-CV.pdf`

## Contact

- **Email:** oladipupod913@gmail.com
- **Phone / WhatsApp:** +234 902 944 0091
- **GitHub:** [github.com/ADIAMO777](https://github.com/ADIAMO777)
- **LinkedIn:** [bankole-adiamo-9a563232b](https://www.linkedin.com/in/bankole-adiamo-9a563232b/)
- **X:** [@AdiamoB](https://x.com/AdiamoB)

## Post-Deploy Checklist

After pushing to GitHub (Vercel auto-deploys):

1. Test the live site — links, contact form, CV download, mobile nav
2. [Google Search Console](https://search.google.com/search-console) — verify domain and submit `sitemap.xml`
3. [Vercel Dashboard](https://vercel.com) — enable Analytics (script is already in `index.html`)

## License

© 2026 ADIAMO BANKOLE. All rights reserved.
