const toggle = document.getElementById("menu-toggle");
const navLinks = document.querySelector(".nav-links");

toggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

function toggleMode() {
    document.body.classList.toggle("dark");

    let btn = document.getElementById("modeBtn");
    btn.innerText = document.body.classList.contains("dark")
        ? "Light Mode"
        : "Dark Mode";
}