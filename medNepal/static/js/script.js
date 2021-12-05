const navMenu = document.querySelector(".navi-menu");
const navigation = document.querySelector(".navi-bar");

navMenu.addEventListener("click", () => {
  navigation.classList.toggle("open");
  navMenu.classList.toggle("open-menu");
  console.log("hello");
});

console.log("hello");