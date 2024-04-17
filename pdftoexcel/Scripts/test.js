const fetch = require('node-fetch');

const url = 'https://iatacodes-iatacodes-v1.p.rapidapi.com/api/v9/suggest?term=spain';
const options = {
  method: 'GET',
  headers: {
    'X-RapidAPI-Key': '592827f03cmshea78756b672a518p1b2519jsna278bc47addf',
    'X-RapidAPI-Host': 'iatacodes-iatacodes-v1.p.rapidapi.com'
  }
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}