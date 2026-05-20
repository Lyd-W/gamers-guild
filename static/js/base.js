(function () {
    const bttBtn = document.querySelector(".btt-btn");
    if (!bttBtn) return;

    function getActiveScrollable() {
    const games = document.querySelector(".games-scroll");
    const products = document.querySelector(".products-scroll");

    const candidates = [games, products].filter(Boolean);

    for (const el of candidates) {
        const isScrollable = el.scrollHeight > el.clientHeight;
        const isScrolled = el.scrollTop > 0;

        if (
        isScrollable &&
        (isScrolled || document.activeElement === el)
        ) {
        return el;
        }
    }

    return null;
    }

    function getScrollPosition(target) {
    if (target) return target.scrollTop;
    return window.scrollY || document.documentElement.scrollTop;
    }

    function scrollToTop(target) {
    if (target) {
        target.scrollTo({
        top: 0,
        behavior: "smooth",
        });
    } else {
        window.scrollTo({
        top: 0,
        behavior: "smooth",
        });
    }
    }

    function updateBttVisibility() {
    const target = getActiveScrollable();
    const scrollPos = getScrollPosition(target);

    if (scrollPos > 300) {
        bttBtn.classList.add("show");
        bttBtn.style.display = "block";
    } else {
        bttBtn.classList.remove("show");
        bttBtn.style.display = "none";
    }
    }

    function handleClick() {
    const target = getActiveScrollable();
    scrollToTop(target);
    }

    bttBtn.addEventListener("click", handleClick);

    window.addEventListener("scroll", updateBttVisibility);

    document.addEventListener("DOMContentLoaded", () => {
    const games = document.querySelector(".games-scroll");
    const products = document.querySelector(".products-scroll");

    if (games) {
        games.addEventListener("scroll", updateBttVisibility);
    }

    if (products) {
        products.addEventListener("scroll", updateBttVisibility);
    }

    updateBttVisibility();
    });
})();

document.querySelectorAll(".toast").forEach((el) => {
    new bootstrap.Toast(el).show();
});