document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll('.update-link').forEach(link => {
        link.addEventListener('click', function () {

            const form = this.closest('td')?.querySelector('form');

            if (form) {
                form.submit();
            }
        });
    });

    document.querySelectorAll('.remove-item').forEach(button => {
        button.addEventListener('click', function () {

            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const itemId = this.id.split('remove_')[1];
            const size = this.dataset.size;

            const url = `/bag/remove/${itemId}/`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    product_size: size,
                    csrfmiddlewaretoken: csrfToken
                })
            })
            .then(response => {
                if (response.ok) {
                    location.reload();
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });

        });
    });

});