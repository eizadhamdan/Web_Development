document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('form').onsubmit = function() {
        fetch("https://api.exchangeratesapi.io/latest?base=USD&access_key=ACCESS_KEY")
        .then(response => response.json())
        .then(data => {
            const currency = document.querySelector('#currency').value.toUpperCase();
            const rate = data.rates[currency];
            if (rate !== undefined) {
                const result = `1 USD is equal to ${rate.toFixed(3)} ${currency}`;
                document.querySelector('#result').innerHTML = result;
            } else {
                document.querySelector('#result').innerHTML = 'Invalid currency.';
            }
        })
        .catch(error => {
            console.log('Error:', error);
        });
        
        return false;
    }

});