document
.getElementById("sort-selector")
.addEventListener("change", function () {
    const url = new URL(window.location.href);
    const val = this.value;

    if (val === "reset") {
    url.searchParams.delete("sort");
    url.searchParams.delete("direction");
    } else {
    const [sort, direction] = val.split("_");
    url.searchParams.set("sort", sort);
    url.searchParams.set("direction", direction);
    }

    window.location.href = url;
});

const openBtn = document.getElementById("openFiltersBtn");
const closeBtn = document.getElementById("closeFiltersBtn");
const overlay = document.getElementById("filterOverlay");

if (openBtn) {
openBtn.addEventListener("click", () => {
    overlay.classList.add("active");
});
}

if (closeBtn) {
closeBtn.addEventListener("click", () => {
    overlay.classList.remove("active");
});
}

overlay.addEventListener("click", (e) => {
if (e.target === overlay) {
    overlay.classList.remove("active");
}
});