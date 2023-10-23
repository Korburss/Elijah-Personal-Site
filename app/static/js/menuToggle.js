menu = document.getElementById("menu-model");
function toggleMenu() {
    if (menu.classList.contains("menu-model-active")) {
        menu.classList.remove("menu-model-active");
    } else {
        menu.classList.add("menu-model-active");
    }
}