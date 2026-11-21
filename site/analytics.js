/* Google Analytics 4 + cookie notice for every page.
   To switch analytics on, put the Measurement ID from GA4 here (looks like "G-AB12CD34EF").
   While it is "G-XXXXXXXXXX", nothing is loaded and no cookie notice is shown. */
const GA_ID = "G-QT5TJW291V";

(function () {
  if (!/^G-[A-Z0-9]{6,}$/.test(GA_ID) || GA_ID === "G-XXXXXXXXXX") return;

  const KEY = "sharpline-analytics-consent"; // "granted" | "denied"
  const read = () => { try { return localStorage.getItem(KEY); } catch { return null; } };
  const save = (v) => { try { localStorage.setItem(KEY, v); } catch {} };

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };

  // Consent Mode: no analytics cookies until the visitor says OK. Ads storage is never used.
  const choice = read();
  gtag("consent", "default", {
    analytics_storage: choice === "granted" ? "granted" : "denied",
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

  /* ---- cookie notice ---- */
  function setChoice(v) {
    save(v);
    gtag("consent", "update", { analytics_storage: v });
    const bar = document.getElementById("cookie-notice");
    if (bar) bar.remove();
  }

  function showNotice() {
    if (document.getElementById("cookie-notice")) return;
    const root = document.querySelector('link[rel="icon"]').getAttribute("href").replace("favicon.svg", "");
    const bar = document.createElement("div");
    bar.id = "cookie-notice";
    bar.className = "cookie-notice";
    bar.setAttribute("role", "region");
    bar.setAttribute("aria-label", "Cookie notice");
    bar.innerHTML =
      `<p>We use Google Analytics cookies to count visits and see which pages help people. No ads, and we never sell your data. <a href="${root}privacy/">Privacy policy</a></p>` +
      `<div class="cookie-actions"><button type="button" class="btn" data-c="granted">OK</button>` +
      `<button type="button" class="btn btn--ghost" data-c="denied">No thanks</button></div>`;
    bar.addEventListener("click", (e) => { const v = e.target.dataset && e.target.dataset.c; if (v) setChoice(v); });
    document.body.appendChild(bar);
  }

  // Any element with data-cookie-settings (e.g. on the privacy page) re-opens the notice.
  document.addEventListener("click", (e) => {
    const t = e.target.closest && e.target.closest("[data-cookie-settings]");
    if (t) { e.preventDefault(); showNotice(); }
  });

  if (!choice) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", showNotice);
    else showNotice();
  }
})();
