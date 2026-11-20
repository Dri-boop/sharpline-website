/* ===== EDIT THESE ===== */
const CONFIG = {
  whatsapp: "27676177735",            // international format, no "+" or spaces
  waMessage: "Hi Sharpline Renovation & Woodworks, I'd like a quote for ",
  waPhotoMessage: "Hi Sharpline Renovation & Woodworks! I'd like an estimate. I'm sending photos of the space.\nProject: \nSuburb: \nRough measurements: ",
  waAdviceMessage: "Hi Charles, I'd like your advice on a project. Here are some photos of the space.\nWhat I'm thinking of: \nSuburb: ",
};
/* ====================== */

const waLink = (text) =>
  `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(text || CONFIG.waMessage)}`;

document.querySelectorAll("[data-wa]").forEach((a) => {
  a.href = waLink();
  a.target = "_blank";
  a.rel = "noopener";
});
document.querySelectorAll("[data-wa-photo]").forEach((a) => {
  a.href = waLink(CONFIG.waPhotoMessage);
  a.target = "_blank";
  a.rel = "noopener";
});
document.querySelectorAll("[data-wa-advice]").forEach((a) => {
  a.href = waLink(CONFIG.waAdviceMessage);
  a.target = "_blank";
  a.rel = "noopener";
});
document.getElementById("year").textContent = new Date().getFullYear();

/* mobile nav */
const toggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("nav");
toggle.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", open);
});
nav.addEventListener("click", (e) => {
  if (e.target.tagName === "A") { nav.classList.remove("open"); toggle.setAttribute("aria-expanded", false); }
});

/* gallery: filter + "show more" */
const figures = [...document.querySelectorAll("#gallery figure")];
const moreBtn = document.getElementById("more");
const PAGE = 16;
let filter = "all";
let limit = PAGE;

function renderGallery() {
  const matching = figures.filter((f) => filter === "all" || f.dataset.cat === filter);
  figures.forEach((f) => (f.hidden = true));
  matching.forEach((f, i) => (f.hidden = i >= limit));
  moreBtn.parentElement.hidden = matching.length <= limit;
}

const filterBtns = document.querySelectorAll(".filters button");
filterBtns.forEach((btn) => {
  const n = btn.dataset.filter === "all" ? figures.length
    : figures.filter((f) => f.dataset.cat === btn.dataset.filter).length;
  btn.insertAdjacentHTML("beforeend", `<sup>${n}</sup>`);
  btn.addEventListener("click", () => {
    filterBtns.forEach((b) => b.setAttribute("aria-pressed", b === btn));
    filter = btn.dataset.filter;
    limit = PAGE;
    renderGallery();
  });
});
moreBtn.addEventListener("click", () => { limit += PAGE; renderGallery(); });
renderGallery();

/* lightbox */
const lb = document.getElementById("lightbox");
const lbImg = document.getElementById("lb-img");
const lbCap = document.getElementById("lb-cap");
let current = 0;
const visible = () => figures.filter((f) => !f.hidden);

function show(idx) {
  const list = visible();
  current = (idx + list.length) % list.length;
  const img = list[current].querySelector("img");
  lbImg.src = img.dataset.full;
  lbImg.alt = img.alt;
  lbCap.textContent = list[current].querySelector("figcaption").textContent;
}
figures.forEach((f) => {
  const open = () => { show(visible().indexOf(f)); lb.showModal(); };
  f.addEventListener("click", open);
  f.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); } });
});
document.getElementById("lb-prev").onclick = () => show(current - 1);
document.getElementById("lb-next").onclick = () => show(current + 1);
document.getElementById("lb-close").onclick = () => lb.close();
lb.addEventListener("click", (e) => { if (e.target === lb) lb.close(); });
lb.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") show(current - 1);
  if (e.key === "ArrowRight") show(current + 1);
});

/* quote form: Netlify handles it when hosted there; otherwise send via WhatsApp */
const form = document.getElementById("quote");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = new FormData(form);
  const text =
    `Hi Sharpline Renovation & Woodworks, I'd like a quote.\n` +
    `Name: ${data.get("name")}\nPhone: ${data.get("phone")}\n` +
    `Suburb: ${data.get("suburb") || "-"}\nProject: ${data.get("service")}\n` +
    `Details: ${data.get("message") || "-"}`;
  try {
    const res = await fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(data).toString(),
    });
    if (!res.ok) throw new Error(res.status);
    form.innerHTML = `<h3>Thanks, ${data.get("name")}.</h3><p>Your request is in. We'll come back to you with your quote as soon as possible.</p>`;
  } catch {
    const w = window.open(waLink(text), "_blank"); // ("noopener" would make this always return null)
    if (w) w.opener = null;
    if (!w) location.href = waLink(text); // pop-up blocked: go straight to WhatsApp
  }
});

/* reveal on scroll */
const io = new IntersectionObserver((entries) => {
  entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
}, { threshold: 0.15 });
document.querySelectorAll(".reveal").forEach((el, i) => {
  el.style.transitionDelay = `${(i % 3) * 80}ms`;
  io.observe(el);
});

/* only play videos while they are on screen */
const vidObserver = new IntersectionObserver((entries) => {
  entries.forEach((en) => { en.isIntersecting ? en.target.play().catch(() => {}) : en.target.pause(); });
}, { threshold: 0.3 });
document.querySelectorAll("video").forEach((v) => vidObserver.observe(v));
