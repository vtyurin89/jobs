   // Necessary global variables
var config = {
    apiUrLPart1: 'https://api.countrystatecity.in/v1/countries/',
    apiUrLPart2: '/cities',
    apiKey: 'VUpsZ003Sk56T1E0UUNkUVVBSTEya01Id0c3dE5IejhNSGFKekFGNA==',
    cityList: [],
}


// Main function starts after the DOM was loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');


    // City dropdown thing was not part of the django form, so add it now
    addDropdown();


    // Load initial list of cities
    getCityList();

    // Changing the country creates a new list
    const cityInput = document.getElementById('city');
    document.getElementById('country').addEventListener('change', () => getCityList());

    // Dynamic search for cities
    cityInput.addEventListener("input", () => dynamicInputChange(cityInput));



})

//Function requests all cities of a country and turns them into a list of names
async function getCityList() {
    const clearCity = document.getElementById('city');
    clearCity.value = "";

    var newCountry = document.getElementById('country').value;
    if (newCountry == 'None') {
        // pass;
    } else {
        let ApiURL = config.apiUrLPart1 + newCountry + config.apiUrLPart2;
    const data = await fetch(ApiURL, {headers: {"X-CSCAPI-KEY": config.apiKey}});
    const citiesJson = await data.json();
    config.cityList = citiesJson.map((city) => {
        return city.name;
    })
    delete citiesJson;
    }
}


// Creates the dropdown html element
function addDropdown() {
    const dropDown = document.createElement('div');
    dropDown.classList.add('dropdown-wrapper');
    dropDown.innerHTML = `
        <ul id="dropdown-autocomplete-list">
        </ul>
    `;
    var newCountry = document.getElementById('city');
    newCountry.after(dropDown);
}


// Temporary function to filter cities according to the user's input
function dynamicInputChange(cityInput) {
    const letters = cityInput.value.toLowerCase();

    var filteredCities = [];
    if (letters.length != 0) {
            config.cityList.forEach((cityStr) => {
        if (cityStr.substr(0, letters.length).toLowerCase() === letters) {
            filteredCities.push(cityStr);
        }
    });
    } else {
        filteredCities = [];
    }

    createDropdown(filteredCities, letters);
}


// Generate dropdown element with a list of filtered cities as buttons
function createDropdown(filteredCities, letters) {
    const cityDropdown = document.getElementById('dropdown-autocomplete-list');
    cityDropdown.innerHTML = '';
    if (letters.length == 0) {
        cityDropdown.innerHTML = '';
    } else {
        filteredCities.forEach((city) => {
            const dropdownOption = document.createElement('li');
            const chooseCityButton = document.createElement('button');
            chooseCityButton.classList.add('w-100');
            chooseCityButton.innerHTML = city;
            chooseCityButton.addEventListener('click', clickButtonToChooseCity);
            dropdownOption.appendChild(chooseCityButton);
            cityDropdown.appendChild(dropdownOption);
    });
    }
}


// Deletes dropdown when no longer needed
function deleteDropdown() {
    const cityDropdown = document.getElementById('dropdown-autocomplete-list');
    cityDropdown.innerHTML = '';
}


// Clicking the corresponding city puts its value in the input field
function clickButtonToChooseCity(e) {
    e.preventDefault();
    const cityButton = e.target;
    const cityInput = document.getElementById('city');
    cityInput.value = cityButton.innerHTML;
    deleteDropdown();
}


// Gets token from cookie
function getTokenFromCookie(token) {
    const cookie = `; ${document.cookie}`;
    const components = cookie.split(`; ${token}=`);
    if (components.length == 2) return components.pop().split(';').shift();
}


