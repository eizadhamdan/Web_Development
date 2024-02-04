let counter = 0;
            
function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').addEventListener('click', count);

    // run every 1000ms
    setInterval(count, 1000);
});
