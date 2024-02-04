document.addEventListener('DOMContentLoaded', function() {
    
    // By default, submit button should be disabled
    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
        
    }

    document.querySelector('form').onsubmit = () => {
        const task = document.querySelector('#task').value;
        console.log(task);

        const list_item = document.createElement('li');
        list_item.innerHTML = task;

        document.querySelector('#tasks').append(list_item);

        document.querySelector('#task').value = '';
        document.querySelector('#submit').disabled = true;

        // Stop form from submitting
        return false;
    }

});