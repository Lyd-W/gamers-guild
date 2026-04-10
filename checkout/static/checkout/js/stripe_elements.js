var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
var client_secret = document.getElementById('id_client_secret').textContent.slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#E6E6E6',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {
    style: style,
    hidePostalCode: true
});
card.mount('#card-element');