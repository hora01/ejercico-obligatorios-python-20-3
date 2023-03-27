const menudeple = document.querySelector(".menudeple");
const menu = document.querySelector(".menu-navegacion");

console.log(menu);
console.log(menudeple);

menudeple.addEventListener("click", () => {
  menu.classList.toggle("spread");
});

window.addEventListener("click", (e) => {
  if (
    menu.classList.contains("spread") &&
    e.target != menu &&
    e.target != menudeple
  )
    menu.classList.toggle("spread");
});
