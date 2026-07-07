"""Generate ADIAMO BANKOLE CV PDF. Run: python assets/generate-cv.py"""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "ADIAMO-BANKOLE-CV.pdf"
PHOTO = ROOT / "profile.jpg"

INDIGO = (67, 56, 202)
TEAL = (13, 148, 136)
GOLD = (202, 138, 4)
DARK = (30, 41, 59)
MUTED = (100, 116, 139)
WHITE = (255, 255, 255)


class CV(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*MUTED)
        self.cell(
            0,
            8,
            "ADIAMO BANKOLE  |  Software Developer CV  |  Page " + str(self.page_no()),
            align="C",
        )


def section_title(pdf, title):
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*INDIGO)
    pdf.cell(0, 8, title.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*TEAL)
    pdf.set_line_width(0.6)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)


def body_text(pdf, text, bold=False):
    pdf.set_font("Helvetica", "B" if bold else "", 10)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(0, 5.5, text)
    pdf.ln(1)


def bullet(pdf, text):
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*DARK)
    x = pdf.get_x()
    pdf.cell(5, 5.5, "-")
    pdf.multi_cell(0, 5.5, text)
    pdf.set_x(x)


def project_entry(pdf, name, desc, live, github):
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 6, name, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(0, 5, desc)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEAL)
    pdf.cell(0, 4, f"Live: {live}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(*INDIGO)
    pdf.cell(0, 4, f"Code: {github}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)


def draw_header(pdf):
    pdf.set_fill_color(*INDIGO)
    pdf.rect(0, 0, 210, 44, "F")

    if PHOTO.exists():
        pdf.image(str(PHOTO), x=168, y=7, w=32, h=32)

    pdf.set_xy(10, 10)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*WHITE)
    pdf.cell(145, 10, "ADIAMO BANKOLE", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(10)
    pdf.set_font("Helvetica", "", 13)
    pdf.set_text_color(*GOLD)
    pdf.cell(145, 8, "Software Developer", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(10)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(226, 232, 240)
    pdf.cell(145, 5, "Nigeria  |  Open to Work  |  Remote & On-site", new_x="LMARGIN", new_y="NEXT")


def skill_category(pdf, name, items):
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 5, name, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(0, 5, ", ".join(items))
    pdf.ln(1)


def build_cv():
    pdf = CV()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    draw_header(pdf)

    pdf.set_y(50)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*DARK)
    contact = (
        "Email: oladipupod913@gmail.com\n"
        "Phone / WhatsApp: +234 902 944 0091\n"
        "Portfolio: portfolio-2025-five-silk.vercel.app\n"
        "GitHub: github.com/ADIAMO777\n"
        "LinkedIn: linkedin.com/in/bankole-adiamo-9a563232b\n"
        "X: x.com/AdiamoB"
    )
    pdf.multi_cell(0, 5, contact)
    pdf.ln(4)

    section_title(pdf, "Professional Summary")
    body_text(
        pdf,
        "Dedicated software developer specializing in responsive, modern, and scalable web "
        "applications. I build reliable, user-centered digital products with HTML, CSS, JavaScript, "
        "and modern deployment workflows using Vercel, Netlify, and GitHub. Focused on clean code, "
        "clear communication, and delivering measurable value for clients.",
    )

    section_title(pdf, "Skills")
    skill_categories = [
        (
            "Frontend Development",
            [
                "HTML5",
                "CSS3",
                "JavaScript (ES6+)",
                "Responsive Web Design",
                "Bootstrap",
                "Tailwind CSS",
                "React",
            ],
        ),
        (
            "Backend Development",
            ["Node.js", "Express.js", "Python", "C# (.NET)"],
        ),
        (
            "Database Management",
            ["MySQL", "PostgreSQL", "MongoDB"],
        ),
        (
            "Version Control & Deployment",
            ["Git & GitHub", "GitHub Actions"],
        ),
        (
            "Operating Systems",
            ["Windows", "Linux (Ubuntu)"],
        ),
        (
            "Command Line",
            ["Bash", "PowerShell", "Linux Terminal"],
        ),
        (
            "Package Managers",
            ["npm", "pnpm", "Yarn"],
        ),
        (
            "UI/UX Basics",
            ["Figma"],
        ),
        (
            "Soft Skills",
            [
                "Communication",
                "Teamwork",
                "Time Management",
                "Adaptability",
                "Critical Thinking",
                "Attention to Detail",
            ],
        ),
        (
            "Professional Practices",
            [
                "Documentation",
                "Code Reviews",
                "Clean Code Principles",
                "Design Patterns",
            ],
        ),
        (
            "Essential Tools",
            [
                "Visual Studio Code",
                "Chrome DevTools",
                "Postman",
                "Git",
            ],
        ),
    ]
    for name, items in skill_categories:
        skill_category(pdf, name, items)
    pdf.ln(1)

    section_title(pdf, "Education & Training")
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 6, "Front-End Engineering - Cohort 1", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*MUTED)
    pdf.cell(
        0,
        5,
        "Intensive training in HTML, CSS, JavaScript, responsive design, and project deployment.",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(3)

    section_title(pdf, "Selected Projects")
    project_entry(
        pdf,
        "SwiftCore Solutions",
        "Business website for a solar energy company and tech school: services, pricing plans, "
        "battery storage, and web development packages.",
        "swift-core-service.netlify.app",
        "github.com/ADIAMO777/SWIFT-CORE-ORIGINAL",
    )
    project_entry(
        pdf,
        "La Bella-Bites",
        "Restaurant website showcasing menu items, descriptions, serving styles, and pricing.",
        "la-bella-bites.vercel.app",
        "github.com/ADIAMO777/LA-BELLA-BITES",
    )
    project_entry(
        pdf,
        "Responsive Nav-Bar",
        "Modern portfolio with fully responsive navigation and mobile toggle menu.",
        "assignment-01-five-chi.vercel.app",
        "github.com/ADIAMO777/Assignment-01",
    )
    project_entry(
        pdf,
        "Web App UI",
        "Interactive web app with dynamic text color changes using HTML and JavaScript.",
        "exercise-class.netlify.app",
        "github.com/ADIAMO777/Exercise-01",
    )

    section_title(pdf, "Services")
    body_text(
        pdf,
        "Landing pages, business websites, responsive redesigns, UI/UX implementation, deployment, and site maintenance.",
    )

    section_title(pdf, "Languages")
    body_text(pdf, "English (Professional)")

    pdf.output(str(OUTPUT))
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    build_cv()
