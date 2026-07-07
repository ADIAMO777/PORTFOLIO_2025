const toggle = document.getElementById("menu-toggle");
const navLinks = document.querySelector(".nav-links");
const header = document.querySelector("header");
const scrollProgress = document.getElementById("scroll-progress");
const scrollTopBtn = document.getElementById("scroll-top");
const modeBtn = document.getElementById("modeBtn");

// Mobile menu toggle
toggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => navLinks.classList.remove("active"));
});

// Dark / Light mode
function toggleMode() {
  document.body.classList.toggle("dark");
  const isDark = document.body.classList.contains("dark");
  modeBtn.textContent = isDark ? "Light Mode" : "Dark Mode";
  localStorage.setItem("theme", isDark ? "dark" : "light");
}

modeBtn.addEventListener("click", toggleMode);

if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark");
  modeBtn.textContent = "Light Mode";
}

// Scroll progress bar
window.addEventListener("scroll", () => {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
  scrollProgress.style.width = progress + "%";

  header.classList.toggle("scrolled", scrollTop > 50);
  scrollTopBtn.classList.toggle("visible", scrollTop > 400);
});

scrollTopBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

// Typing effect
const typingEl = document.getElementById("typing-text");
const phrases = [
  "modern web interfaces",
  "responsive designs",
  "interactive experiences",
  "clean UI/UX",
];
let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeEffect() {
  const current = phrases[phraseIndex];

  if (isDeleting) {
    typingEl.textContent = current.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typingEl.textContent = current.substring(0, charIndex + 1);
    charIndex++;
  }

  let speed = isDeleting ? 40 : 80;

  if (!isDeleting && charIndex === current.length) {
    speed = 2000;
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    phraseIndex = (phraseIndex + 1) % phrases.length;
    speed = 500;
  }

  setTimeout(typeEffect, speed);
}

typeEffect();

// Scroll reveal with Intersection Observer
const revealElements = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        const delay = entry.target.dataset.delay
          ? parseInt(entry.target.dataset.delay, 10) * 120
          : index * 100;
        setTimeout(() => entry.target.classList.add("active"), delay);
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15, rootMargin: "0px 0px -50px 0px" }
);

revealElements.forEach((el) => revealObserver.observe(el));

// Skill bar animation
const skillFills = document.querySelectorAll(".skill-fill");

const skillObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const fill = entry.target;
        const width = fill.dataset.width;
        fill.style.width = width + "%";

        const pct = fill.closest(".skill-card")?.querySelector(".skill-pct");
        if (pct) {
          animatePct(pct, parseInt(pct.dataset.target, 10));
        }

        skillObserver.unobserve(fill);
      }
    });
  },
  { threshold: 0.5 }
);

skillFills.forEach((fill) => skillObserver.observe(fill));

// Counter animation for stats
const statNumbers = document.querySelectorAll(".stat-number");

const counterObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.dataset.target, 10);
        animateCounter(entry.target, target);
        counterObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.5 }
);

statNumbers.forEach((stat) => counterObserver.observe(stat));

function animateCounter(el, target) {
  animatePct(el, target, false);
}

function animatePct(el, target, withSuffix = true) {
  let current = 0;
  const increment = target / 60;
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      el.textContent = withSuffix ? target + "%" : target;
      clearInterval(timer);
    } else {
      el.textContent = withSuffix
        ? Math.floor(current) + "%"
        : Math.floor(current);
    }
  }, 25);
}

// Active nav link on scroll
const sections = document.querySelectorAll("section[id]");
const navLinkEls = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {
  const scrollY = window.scrollY + 100;

  sections.forEach((section) => {
    const top = section.offsetTop;
    const height = section.offsetHeight;
    const id = section.getAttribute("id");

    if (scrollY >= top && scrollY < top + height) {
      navLinkEls.forEach((link) => {
        link.classList.remove("active");
        if (link.getAttribute("href") === "#" + id) {
          link.classList.add("active");
        }
      });
    }
  });
});

// 3D tilt on skill cards
document.querySelectorAll("[data-tilt]").forEach((card) => {
  card.addEventListener("mousemove", (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateX = (y - centerY) / 15;
    const rotateY = (centerX - x) / 15;

    card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
  });

  card.addEventListener("mouseleave", () => {
    card.style.transform = "";
  });
});

// Project filter
const filterBtns = document.querySelectorAll(".filter-btn");
const projectCards = document.querySelectorAll(".project-card[data-category]");

filterBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const filter = btn.dataset.filter;

    filterBtns.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");

    projectCards.forEach((card) => {
      const categories = card.dataset.category.split(" ");
      const show = filter === "all" || categories.includes(filter);
      card.classList.toggle("hidden", !show);
    });
  });
});

// Contact form — Formspree
const contactForm = document.querySelector(".contact-form");
const formStatus = document.getElementById("form-status");

contactForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const btn = contactForm.querySelector(".btn");
  const originalText = btn.textContent;
  const formData = new FormData(contactForm);

  btn.disabled = true;
  btn.textContent = "Sending...";
  formStatus.textContent = "";
  formStatus.className = "form-status";

  try {
    const response = await fetch(contactForm.action, {
      method: "POST",
      body: formData,
      headers: { Accept: "application/json" },
    });

    const data = await response.json();

    if (response.ok) {
      btn.textContent = "Message Sent! ✓";
      btn.style.background = "linear-gradient(135deg, #28a745, #20c997)";
      formStatus.textContent = "Thanks! I'll get back to you soon.";
      formStatus.classList.add("success");
      contactForm.reset();
    } else {
      throw new Error(data.error || "Something went wrong.");
    }
  } catch (error) {
    btn.textContent = "Try Again";
    formStatus.textContent = error.message || "Failed to send. Please try again.";
    formStatus.classList.add("error");
  }

  setTimeout(() => {
    btn.disabled = false;
    btn.textContent = originalText;
    btn.style.background = "";
  }, 4000);
});
