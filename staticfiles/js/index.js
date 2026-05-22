$(document).ready(function () {

    $('#sort-selector').on('change', function () {

        const currentUrl = new URL(window.location.href);
        const selectedVal = $(this).val();

        if (selectedVal !== "reset") {
            const parts = selectedVal.split("_");
            const direction = parts.pop();
            const sort = parts.join("_");

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
        }

        window.location.replace(currentUrl);
    });

    window.syncFromSlider = function (value) {
        $('#playtimeInput').val(value);
    };

    window.syncFromInput = function (value) {
        let val = parseInt(value) || 0;

        if (val < 0) val = 0;
        if (val > 300) val = 300;

        $('#playtimeSlider').val(val);
    };

});

const openBtn = document.getElementById('openFiltersBtn');
const closeBtn = document.getElementById('closeFiltersBtn');
const overlay = document.querySelector('.filter-overlay-container');

if (openBtn && overlay) {
  openBtn.addEventListener('click', () => {
    overlay.classList.add('active');
  });
}

if (closeBtn && overlay) {
  closeBtn.addEventListener('click', () => {
    overlay.classList.remove('active');
  });
}

if (overlay) {
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) {
      overlay.classList.remove('active');
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {

  const genreCollapse = document.getElementById('desktopGenre');

  if (!genreCollapse) return;

  if (localStorage.getItem('genreAccordionOpen') === 'true') {
    genreCollapse.classList.add('show');
  }

  genreCollapse.addEventListener('shown.bs.collapse', () => {
    localStorage.setItem('genreAccordionOpen', 'true');
  });

  genreCollapse.addEventListener('hidden.bs.collapse', () => {
    localStorage.setItem('genreAccordionOpen', 'false');
  });

});