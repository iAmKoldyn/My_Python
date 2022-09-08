// method to catch weather data from openweathermap.org by city-name

const fs = require('fs');
const path = require('path');

const weatherData = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', '..', 'data', 'weather.json')));

const weather = weatherData.weather;

const city = weatherData.city;

const temperature = weatherData.temp;

const wind = weatherData.wind;

const windSpeed = weatherData.windSpeed;    


console.log(weather);

console.log(city);

console.log(temperature);

console.log(wind);

console.log(windSpeed);

console.log(wind);

console.log(windSpeed);
