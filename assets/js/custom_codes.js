// header
const header = document.getElementById("site-header");

window.addEventListener("scroll", () => {
  if (window.scrollY > 20) header.classList.add("scrolled");
  else header.classList.remove("scrolled");
});
