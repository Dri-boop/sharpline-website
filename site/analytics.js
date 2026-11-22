/* Google Analytics 4 for every page (no cookie banner).
   Visits are counted by default; the privacy page has a "Turn off statistics" button.
   While GA_ID is "G-XXXXXXXXXX", nothing is loaded. */
const GA_ID = "G-QT5TJW291V";

(function () {
  if (!/^G-[A-Z0-9]{6,}$/.test(GA_ID) || GA_ID === "G-XXXXXXXXXX") return;

  const KEY = "sharpline-analytics-consent"; // "granted" | "denied"
  const read = () => { try { return localStorage.getItem(KEY); } catch { return null; } };
  const save = (v) => { try { localStorage.setItem(KEY, v); } catch {} };

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };

  // Consent Mode: analytics on unless the visitor turned it off on the privacy page. Ads storage is never used.
  const choice = read();
  gtag("consent", "default", {
    analytics_storage: choice === "denied" ? "denied" : "granted",
    ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
  });
  gtag("js", new Date());
  gtag("config", GA_ID, { anonymize_ip: true });

  const s = document.createElement("script");
  s.async = true;
  s.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
  document.head.appendChild(s);

  /* ---- events: WhatsApp clicks, phone clicks, quote form ---- */
  const WA_TYPES = [["waPhoto", "photo"], ["waArea", "area"], ["waAdvice", "advice"], ["wa", "general"]];
  document.addEventListener("click", (e) => {
    const a = e.target.closest && e.target.closest("a");
    if (!a) return;
    const href = a.getAttribute("href") || "";
    const wa = WA_TYPES.find(([k]) => k in a.dataset);
    if (wa || href.includes("wa.me/")) {
      gtag("event", "whatsapp_click", {
        link_type: wa ? wa[1] : "general",
        link_text: (a.textContent || a.getAttribute("aria-label") || "").trim().slice(0, 60),
      });
    } else if (href.startsWith("tel:")) {
      gtag("event", "phone_click", { link_text: (a.textContent || "").trim().slice(0, 60) });
    }
  }, true);

  const form = document.getElementById("quote");
  if (form) {
    form.addEventListener("submit", () => {
      const service = new FormData(form).get("service") || "";
      gtag("event", "quote_form_submit", { service: String(service).slice(0, 60) });
    }, true);
  }

  /* ---- opt-out (privacy page) ---- */
  // Buttons with data-analytics-optout turn statistics off (or back on) for this browser.
  function label(btn) { btn.textContent = read() === "denied" ? "Turn statistics back on" : "Turn off statistics"; }
  function initOptout() { document.querySelectorAll("[data-analytics-optout]").forEach(label); }
  document.addEventListener("click", (e) => {
    const t = e.target.closest && e.target.closest("[data-analytics-optout]");
    if (!t) return;
    e.preventDefault();
    const v = read() === "denied" ? "granted" : "denied";
    save(v);
    gtag("consent", "update", { analytics_storage: v });
    label(t);
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initOptout);
  else initOptout();
})();
