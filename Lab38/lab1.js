function parseJSON(jsonStr) {
    try {
        const obj = JSON.parse(jsonStr);
        console.log(obj);
    } catch {
        console.error("Invalid JSON format");
    }
}

parseJSON('{"name": "Alice", "age": 25}');
parseJSON('{name: Alice, age: 25}');