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

/* "In motion jobs": swipeable viewer. Only the job in view plays; the next one peeks in. */
const jobsTrack = document.querySelector(".jobs-track");
if (jobsTrack) {
  const jobs = [...jobsTrack.querySelectorAll(".job")];
  const count = document.querySelector(".jobs-count");
  const dots = [...document.querySelectorAll("[data-jobs-dot]")];
  let current = 0, sectionVisible = false;
  const setActive = (i) => {
    current = i;
    jobs.forEach((j, k) => {
      j.classList.toggle("is-active", k === i);
      const v = j.querySelector("video");
      if (k === i && sectionVisible) { v.preload = "auto"; v.play().catch(() => {}); } else v.pause();
    });
    dots.forEach((d, k) => d.setAttribute("aria-selected", k === i));
    if (count) count.textContent = `${i + 1} / ${jobs.length}`;
  };
  const goTo = (i) => {
    i = Math.max(0, Math.min(jobs.length - 1, i));
    jobsTrack.scrollTo({ left: jobs[i].offsetLeft - jobs[0].offsetLeft, behavior: "smooth" });
  };
  const slideObserver = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) setActive(jobs.indexOf(en.target)); });
  }, { root: jobsTrack, threshold: 0.6 });
  jobs.forEach((j) => slideObserver.observe(j));
  document.querySelector("[data-jobs-prev]").addEventListener("click", () => goTo(current - 1));
  document.querySelector("[data-jobs-next]").addEventListener("click", () => goTo(current + 1));
  dots.forEach((d, k) => d.addEventListener("click", () => goTo(k)));
  jobs.forEach((j, k) => j.addEventListener("click", () => { if (k !== current) goTo(k); }));
  jobsTrack.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") { e.preventDefault(); goTo(current + 1); }
    if (e.key === "ArrowLeft") { e.preventDefault(); goTo(current - 1); }
  });
  new IntersectionObserver(([en]) => { sectionVisible = en.isIntersecting; setActive(current); }, { threshold: 0.25 })
    .observe(jobsTrack);
}

/* "Recent work areas": show half the list, expand on click */
document.querySelectorAll("[data-areas-toggle]").forEach((btn) => {
  const box = btn.closest(".areas");
  btn.addEventListener("click", () => {
    const open = box.classList.toggle("areas--open");
    btn.setAttribute("aria-expanded", open);
    btn.textContent = open ? "Show fewer areas ↑" : `Show all ${btn.dataset.count} areas ↓`;
  });
});

/* "Who we are" team carousel */
const teamTrack = document.querySelector(".team-track");
if (teamTrack) {
  const slides = [...teamTrack.querySelectorAll(".team-slide")];
  const count = document.querySelector(".team-count");
  let cur = 0;
  const goTo = (i) => {
    cur = (i + slides.length) % slides.length;
    teamTrack.scrollTo({ left: slides[cur].offsetLeft - slides[0].offsetLeft, behavior: "smooth" });
  };
  const obs = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) { cur = slides.indexOf(en.target); if (count) count.textContent = `${cur + 1} / ${slides.length}`; }
    });
  }, { root: teamTrack, threshold: 0.6 });
  slides.forEach((sl) => obs.observe(sl));
  document.querySelector("[data-team-prev]").addEventListener("click", () => goTo(cur - 1));
  document.querySelector("[data-team-next]").addEventListener("click", () => goTo(cur + 1));
  teamTrack.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") { e.preventDefault(); goTo(cur + 1); }
    if (e.key === "ArrowLeft") { e.preventDefault(); goTo(cur - 1); }
  });
}
