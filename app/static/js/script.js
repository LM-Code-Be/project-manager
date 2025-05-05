// ---------------------------------------------
// Auteur   : LM-Code
// Site     : https://lm-code.be
// GitHub   : https://github.com/LM-Code-Be
// Projet   : Project Manager (Flask + MySQL)
// ---------------------------------------------


// ————— Flash messages auto‑dismiss —————
$(function () {
  $(".alert").each(function () {
    const alertEl = bootstrap.Alert.getOrCreateInstance(this);
    setTimeout(() => alertEl.close(), 5000);
  });
});

// ————— Tooltips Bootstrap 5 —————
document.querySelectorAll("[data-bs-toggle='tooltip']")
  .forEach(el => new bootstrap.Tooltip(el));
