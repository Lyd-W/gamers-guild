$(document).ready(function () {

    $('.update-link').on('click', function () {
        const form = $(this).closest('td').find('form');
        if (form.length) {
            form.submit();
        }
    });

    $('.remove-item').on('click', function () {

        const csrfToken = "{{ csrf_token }}";
        const itemId = $(this).attr('id').split('remove_')[1];
        const size = $(this).data('size');

        const url = `/bag/remove/${itemId}/`;

        $.ajax({
            url: url,
            type: 'POST',
            data: {
                product_size: size,
                csrfmiddlewaretoken: csrfToken
            },
            success: function () {
                location.reload();
            }
        });
    });

});