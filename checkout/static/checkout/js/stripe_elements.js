const stripePublicKey = document
    .getElementById('id_stripe_public_key')
    .textContent.slice(1, -1);

const clientSecret = document
    .getElementById('id_client_secret')
    .textContent.slice(1, -1);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

const style = {
    base: {
        color: '#E6E6E6',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#D4AF37'
        }
    },
    invalid: {
        color: '#B63E3E',
        iconColor: '#B63E3E'
    }
};

const card = elements.create('card', {
    style: style,
    hidePostalCode: true
});

card.mount('#card-element');

card.addEventListener('change', function (event) {

    const errorDiv = document.getElementById('card-errors');

    if (event.error) {

        const html = `
            <span class="icon" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" 
                     width="16" 
                     height="16" 
                     fill="currentColor" 
                     class="bi bi-x-lg" 
                     viewBox="0 0 16 16">
                    <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
                </svg>
            </span>
            <span>${event.error.message}</span>
        `;

        errorDiv.innerHTML = html;

    } else {
        errorDiv.textContent = '';
    }
});

const form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {

    ev.preventDefault();

    card.update({ disabled: true });

    document.getElementById('submit-button').disabled = true;

    document.getElementById('payment-form')
        .classList.toggle('d-none');

    document.getElementById('loading-overlay')
        .classList.toggle('d-none');

    const saveInfo = document.getElementById('id-save-info').checked;

    const csrfToken = document.querySelector(
        '[name=csrfmiddlewaretoken]'
    ).value;

    const postData = {
        csrfmiddlewaretoken: csrfToken,
        client_secret: clientSecret,
        save_info: saveInfo,
    };

    const url = '/checkout/cache_checkout_data/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams(postData)
    })
    .then(response => {

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        return stripe.confirmCardPayment(clientSecret, {

            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        state: form.county.value.trim(),
                        country: form.country.value.trim(),
                    }
                }
            },

            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim(),
                    country: form.country.value.trim(),
                }
            },

        });
    })
    .then(function (result) {

        if (result.error) {

            const errorDiv = document.getElementById('card-errors');

            const html = `
                <span class="icon" role="alert">
                    <svg xmlns="http://www.w3.org/2000/svg" 
                        width="16" 
                        height="16" 
                        fill="currentColor" 
                        class="bi bi-x-lg" 
                        viewBox="0 0 16 16">
                        <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
                    </svg>
                </span>
                <span>${result.error.message}</span>
            `;

            errorDiv.innerHTML = html;

            document.getElementById('payment-form')
                .classList.toggle('d-none');

            document.getElementById('loading-overlay')
                .classList.toggle('d-none');

            card.update({ disabled: false });

            document.getElementById('submit-button')
                .disabled = false;

        } else if (result.paymentIntent.status === 'succeeded') {

            form.submit();
        }
    })
    .catch(function () {

        location.reload();
    });
});