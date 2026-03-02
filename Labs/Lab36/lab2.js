let message = "Hello from global";

function helloGlobal() {
    let message = "Hello from function scope";
    console.log(message);
}

helloGlobal();
console.log(message);
console.log(localMessage);