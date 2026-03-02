function fetchData() {
    return new Promise(resolve => {
        setTimeout(() => resolve("Data received"), 2000);
    });
}

fetchData()
    .then(result => console.log(result))
    .finally(() => console.log("Request completed"));