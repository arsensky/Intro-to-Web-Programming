function counter() {
    let count = 0;
    return function() {
        count++;
        console.log(count);
    };
}

const count1 = counter();
count1();
count1();

const count2 = counter();
count2();