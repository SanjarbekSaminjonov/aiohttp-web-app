const button = document.querySelector('.main-button');

const number = document.querySelector('.number')


fetch("http://localhost:8000/get", {
    method: 'GET',
    redirect: 'follow'
})
    .then(response => response.json())
    .then(result => {
        number.textContent = result.count;
    })
    .catch(error => console.log('error', error));


button.addEventListener('click', () => {
    fetch("http://localhost:8000/add", {
        method: 'POST',
        redirect: 'follow'
    })
        .then(response => response.json())
        .then(result => {
            number.textContent = result.count;
        })
        .catch(error => console.log('error', error));
});
