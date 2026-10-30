# ADIAMO BANKOLE — Software Developer Portfolio

Personal portfolio website for **ADIAMO BANKOLE**, a software developer based in Nigeria. Built with HTML, CSS, and vanilla JavaScript — no frontend framework — optimized for performance, SEO, and client conversions.

---

## Live Links

| Resource | URL |
|----------|-----|
| **Portfolio (live)** | [bankole-dev.vercel.app](https://bankole-dev.vercel.app) |
| **GitHub repository** | [github.com/ADIAMO777/PORTFOLIO_2025](https://github.com/ADIAMO777/PORTFOLIO_2025) |
| **Download CV (PDF)** | [assets/ADIAMO-BANKOLE-CV.pdf](https://bankole-dev.vercel.app/assets/ADIAMO-BANKOLE-CV.pdf) |
| **Book a call (Calendly)** | [calendly.com/oladipupod913/30min](https://calendly.com/oladipupod913/30min) |
| **Calendly profile** | [calendly.com/oladipupod913](https://calendly.com/oladipupod913) |

> The previous address `portfolio-2025-five-silk.vercel.app` permanently redirects (308) to `bankole-dev.vercel.app`, so old links keep working.

---

## About

I'm **ADIAMO BANKOLE**, a software developer available for freelance projects, business websites, and web applications (remote and on-site). The portfolio highlights skills, delivered projects, client testimonials, a case-study blog post, and direct contact options.

---

## Site Sections

| Section | Description |
|---------|-------------|
| **Hero** | Profile photo, Software Developer title, typing effect, stats, CV download, Calendly booking |
| **About** | Professional bio and photo |
| **Skills** | 11 categories (frontend, backend, databases, tools, soft skills, etc.) |
| **Services** | Landing pages, business sites, redesign, UI/UX, deployment, maintenance |
| **Projects** | 6 portfolio projects with case studies (problem → solution → tech → result) |
| **Testimonials** | Client feedback with star ratings |
| **Blog** | Featured article: *How I Built SwiftCore Solutions' Business Website* |
| **Contact** | Calendly booking; Formspree contact form beside a Contact & Info card (email with Copy button, WhatsApp, GitHub/LinkedIn/X); light/dark mode toggle |
| **Footer** | Copyright |

---

## Features

- Responsive layout with a keyboard-accessible mobile menu
- Navbar hover highlight, with an underline marking the current section
- Scroll progress bar, scroll reveal animations, typing effect
- Project filter (All, HTML/CSS, JavaScript, Web Design, Business)
- 11-category skills cards with tag layout
- Project case studies on every portfolio item
- Star-rated testimonials
- Featured blog post (SwiftCore case study)
- **Book a Call** via Calendly (hero + contact section)
- Contact form via Formspree (AJAX submission) with an animated checkmark when the message sends
- Copy-email button with a "Copied!" toast
- Light/dark mode toggle with sun/moon icon; choice is remembered and applied before first paint (no flash)
- Dark mode gold accent shimmer on the hero name
- Brand-colored social icon hovers (GitHub green, LinkedIn blue, X red)
- Downloadable CV (PDF)
- Project screenshots in WebP (~170 KB total)
- SEO: meta tags, Open Graph, Twitter cards, `sitemap.xml`, `robots.txt`
- Google Search Console verified (HTML file + meta tag)
- Custom `404.html` page
- Vercel Analytics integration
- Caching via `vercel.json`: screenshots, favicon and social preview cached for a year; CV, profile photo, `style.css` and `script.js` revalidated on every visit

---

## CV (Both Files)

The project includes **two CV-related files**:

### 1. `assets/ADIAMO-BANKOLE-CV.pdf` (downloadable CV)

- Professional PDF resume linked from the hero **Download CV** button
- Includes: photo, contact info, summary, 11 skill categories, education, 6 projects, services
- Title: **Software Developer**
- Live download: [ADIAMO-BANKOLE-CV.pdf](https://bankole-dev.vercel.app/assets/ADIAMO-BANKOLE-CV.pdf)

### 2. `assets/generate-cv.py` (CV generator script)

- Python script that **regenerates** the PDF from source data
- Uses [fpdf2](https://pypi.org/project/fpdf2/) and `assets/profile.jpg` for the header photo
- Run after updating skills, projects, or contact info:

```bash
pip install fpdf2
python assets/generate-cv.py
```

Output overwrites: `assets/ADIAMO-BANKOLE-CV.pdf`

> **Note:** `assets/process-profile.py` is an optional local script for cropping profile photos — not required to run the site.

---

## Portfolio Projects

| Project | Live Demo | Source Code | Hosted On |
|---------|-----------|-------------|-----------|
| **SwiftCore Solutions** | [swift-core-service.netlify.app](https://swift-core-service.netlify.app/) | Private | Netlify |
| **La Bella-Bites** | [la-bella-bites.vercel.app](https://la-bella-bites.vercel.app/) | [LA-BELLA-BITES](https://github.com/ADIAMO777/LA-BELLA-BITES) | Vercel |
| **Nails by Henny** | [nailsbyhenny.vercel.app](https://nailsbyhenny.vercel.app/) | Private | Vercel |
| **Responsive Nav-Bar** | [assignment-01-five-chi.vercel.app](https://assignment-01-five-chi.vercel.app/) | [Assignment-01](https://github.com/ADIAMO777/Assignment-01) | Vercel |
| **Web App UI** | [exercise-class.netlify.app](https://exercise-class.netlify.app/) | [Exercise-01](https://github.com/ADIAMO777/Exercise-01) | Netlify |
| **MiniBank** | — (runs locally with Docker Compose) | [minibank](https://github.com/ADIAMO777/minibank) | AWS ECR (container images) |

---

## Tech Stack (What We Used)

### Frontend (this repo)

| Technology | Used For |
|------------|----------|
| **HTML5** | Semantic structure, SEO meta tags, accessibility |
| **CSS3** | Custom properties, Grid, Flexbox, animations, dark mode, responsive design |
| **JavaScript (ES6+)** | Mobile nav, dark mode, scroll effects, typing effect, Formspree AJAX, project filters, copy-to-clipboard toast, Intersection Observer |
| **Google Fonts — Inter** | Typography (weights 400, 500, 600, 700) |
| **SVG** | Favicon, social icons, WhatsApp icon |

### Backend / services (external — no server code in repo)

| Service | Used For | Link |
|---------|----------|------|
| **Vercel** | Portfolio hosting, auto-deploy from GitHub, Analytics | [vercel.com](https://vercel.com) |
| **Formspree** | Contact form submissions | [formspree.io/f/mojobleq](https://formspree.io/f/mojobleq) |
| **Calendly** | Client booking / 30-min consultations | [calendly.com/oladipupod913/30min](https://calendly.com/oladipupod913/30min) |
| **Google Search Console** | SEO indexing and sitemap submission | [search.google.com/search-console](https://search.google.com/search-console) |
| **GitHub** | Source control and deployment trigger | [github.com/ADIAMO777](https://github.com/ADIAMO777) |

### Deployment platforms (portfolio projects)

| Platform | Projects Hosted |
|----------|-----------------|
| **Vercel** | Portfolio, La Bella-Bites, Nails by Henny, Responsive Nav-Bar |
| **Netlify** | SwiftCore Solutions, Web App UI |
| **AWS ECR** | MiniBank (private container images) |

### Development tools

| Tool | Used For |
|------|----------|
| **VS Code / Cursor** | Code editor |
| **Git & GitHub** | Version control |
| **Python 3 + fpdf2** | CV PDF generation |
| **Python http.server / Live Server** | Local preview (`localhost:5502`) |

### Design theme

| Mode | Colors |
|------|--------|
| **Light** | Navy/blue professional palette (`#1e40af`, `#2563eb`, `#0f766e`) |
| **Dark** | Slate background with 50% gold accent blend; gold shimmer on hero name |

---

## All Sites & Links We Use

### Personal & portfolio

- Portfolio: [bankole-dev.vercel.app](https://bankole-dev.vercel.app)
- GitHub: [github.com/ADIAMO777](https://github.com/ADIAMO777)
- LinkedIn: [linkedin.com/in/adiamo-bankole-9a563232b](https://www.linkedin.com/in/adiamo-bankole-9a563232b/)
- X (Twitter): [x.com/AdiamoB](https://x.com/AdiamoB)
- Email: [oladipupod913@gmail.com](mailto:oladipupod913@gmail.com)
- WhatsApp: [wa.me/2349029440091](https://wa.me/2349029440091)

### Booking & contact

- Calendly (30 min): [calendly.com/oladipupod913/30min](https://calendly.com/oladipupod913/30min)
- Calendly profile: [calendly.com/oladipupod913](https://calendly.com/oladipupod913)
- Formspree form: [formspree.io/f/mojobleq](https://formspree.io/f/mojobleq)

### SEO & analytics

- Sitemap: [bankole-dev.vercel.app/sitemap.xml](https://bankole-dev.vercel.app/sitemap.xml)
- Robots: [bankole-dev.vercel.app/robots.txt](https://bankole-dev.vercel.app/robots.txt)
- Vercel Analytics: `/_vercel/insights/script.js` (enabled in Vercel dashboard)

---

## Project Structure

```
PORTFOLIO_2025/
├── index.html              # Main portfolio page
├── style.css               # Styles, dark mode, responsive layout
├── script.js               # Interactivity and animations
├── 404.html                # Custom not-found page
├── vercel.json             # Vercel config + asset cache headers
├── sitemap.xml             # SEO sitemap
├── robots.txt              # Search engine crawler rules
├── google008fbab2b56d9c6d.html  # Google Search Console verification (keep it)
├── README.md               # This file
├── .vscode/
│   └── settings.json       # Live Server port (5502)
└── assets/
    ├── profile.jpg         # Hero & about photo (also used in CV)
    ├── favicon.svg         # Site favicon
    ├── og-preview.png      # Social media preview image
    ├── ADIAMO-BANKOLE-CV.pdf    # Downloadable CV (generated)
    ├── generate-cv.py      # Script to regenerate CV PDF
    ├── process-profile.py  # Optional profile photo crop script
    └── projects/
        ├── navbar.webp          # Responsive Nav-Bar screenshot
        ├── labella.webp         # La Bella-Bites screenshot
        ├── nailsbyhenny.webp    # Nails by Henny screenshot
        ├── webapp.webp          # Web App UI screenshot
        ├── swiftcore.webp       # SwiftCore Solutions screenshot
        └── minibank.webp        # MiniBank screenshot
```

---

## Run Locally

```bash
git clone https://github.com/ADIAMO777/PORTFOLIO_2025.git
cd PORTFOLIO_2025
python -m http.server 5502
```

Open [http://localhost:5502](http://localhost:5502) in your browser.

No build step or npm install required for the website.

---

## Promote Your Portfolio

### Pin on GitHub

1. Go to [github.com/ADIAMO777](https://github.com/ADIAMO777)
2. Click **Customize your pins**
3. Select **PORTFOLIO_2025** and **minibank**
4. Save

### Add to LinkedIn Featured

1. Open [LinkedIn profile](https://www.linkedin.com/in/adiamo-bankole-9a563232b/)
2. **Add profile section** → **Featured** → **Link**
3. URL: `https://bankole-dev.vercel.app`
4. Title: **Software Developer Portfolio**

---

## Post-Deploy Checklist

1. Test live site — links, CV download, contact form, Calendly, mobile nav, dark mode
2. [Google Search Console](https://search.google.com/search-console) — property `https://bankole-dev.vercel.app/` is verified and `sitemap.xml` is submitted; use **URL inspection → Request indexing** after big changes
3. [Vercel Dashboard](https://vercel.com) — confirm Analytics is enabled
4. Portfolio link is shared on LinkedIn Featured, GitHub bio, and the CV

## Maintenance Notes

- **Keep** `google008fbab2b56d9c6d.html` and the `google-site-verification` meta tags in `index.html`, or Search Console verification is lost.
- **Replacing a project screenshot?** Use a new filename (e.g. `labella-v2.webp`) — screenshots are cached for a year, so a same-name file won't refresh for returning visitors.
- **Changed skills, projects, or contact info?** Update `assets/generate-cv.py` and run `python assets/generate-cv.py` so the CV matches the site.
- `cleanUrls` is off in `vercel.json` on purpose, so `.html` files (like the Google verification file) are served at their exact path.

---

## License

© 2026 ADIAMO BANKOLE. All rights reserved.
