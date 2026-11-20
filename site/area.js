/* Script for the suburb pages (areas/...). Keep the number in sync with main.js. */
const WHATSAPP = "27676177735";
const area = document.body.dataset.area || "Cape Town";
const wa = (text) => `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(text)}`;

document.querySelectorAll("[data-wa-area]").forEach((a) => {
  a.href = wa(`Hi Sharpline Renovation & Woodworks, I'd like a quote in ${area}. I'm sending photos of the space.\nProject: \nRough measurements: `);
  a.target = "_blank";
  a.rel = "noopener";
});
document.querySelectorAll("[data-wa]").forEach((a) => {
  a.href = wa("Hi Sharpline Renovation & Woodworks, I'd like a quote for ");
  a.target = "_blank";
  a.rel = "noopener";
});

const toggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open);
  });
}
const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();
