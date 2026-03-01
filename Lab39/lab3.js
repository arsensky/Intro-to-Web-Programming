function startCounter() {
    let count = 1;
    const interval = setInterval(() => {
        console.log("Counter:", count);
        if (count === 5) {
            clearInterval(interval);
        }
        count++;
    }, 1000);
}

startCounter();