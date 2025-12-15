const btn = document.querySelector(".hamburger");
const navLinks = document.querySelector("#nav-links");

hamburger.addEventListener("click", () => {
  navLinks.style.display =
    navLinks.style.display === "flex" ? "none" : "flex";
});


function toggleMode() {
    document.body.classList.toggle("dark");

    let btn = document.getElementById("modeBtn");
    btn.innerText = document.body.classList.contains("dark")
        ? "Light Mode"
        : "Dark Mode";
}