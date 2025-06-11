const express = require('express');
const cookieParser = require('cookie-parser');
const app = express()
const port = 8080;

const date = new Date();

app.get('/', (req, res) => {
    res.send('Hello World!');
})

app.get('/about', (req, res) => {
    res.send('This is my express app');
})

app.get('/year', (req, res) => {
    const year = date.getFullYear();
    res.send(`The year is now ${year}`);
})

app.get('/time', (req, res) => {
    const time = date.getTime();
    res.send(`The time is now ${time}`);
})

app.get('/day', (req, res) => {
    const weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    const day = weekday[date.getDay()];
    res.send(`The day is now ${day}`);
})

app.get('/greet', (req, res) => {
    const name = req.query.name;
    res.send(`Hello, ${name}`);
})

app.get('/age', (req, res) => {
    const yearOfBirth = req.query.year;

    let age = date.getFullYear() - parseInt(yearOfBirth);

    res.send(`You are ${age} years old`);
})

app.get('/add', (req, res) => {
    const x = parseFloat(req.query.x);
    const y = parseFloat(req.query.y);
    let sum = x + y;

    res.send(`The sum of the two numbers is ${sum}`);
})

app.get('/multiply', (req, res) => {
    const x = parseFloat(req.query.x);
    const y = parseFloat(req.query.y);
    let sum = x * y;

    res.send(`The product of the two numbers is ${sum}`);
})

app.get('/convert', (req, res) => {
    const inch = parseFloat(req.query.inch);
    let centimeters = inch * 2.54;
    
    res.send(`${inch} inches converts to ${centimeters} centimeters`);

})

app.get('/headers', (req, res) => {
    const userEmail = req.get('user-email');
    const userRole = req.get('user-role');
    const deviceType = req.get('device-type');

    console.log('Headers Received:');
    console.log(userEmail);
    console.log(userRole);
    console.log(deviceType);

    res.json({
        'user-email': userEmail,
        'user-role': userRole,
        'device-type': deviceType
    });
})

app.use(cookieParser());

app.get('/theme', (req, res) => {
    const theme = req.cookies.theme;
    console.log(theme);
    
    res.json({theme});
})

app.listen(port, () => {
    console.log(`Lab 3 App listening on port ${port}`);
})