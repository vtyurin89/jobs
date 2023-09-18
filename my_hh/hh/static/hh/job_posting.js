// Necessary data
var config = {
    apiUrLPart1: 'https://api.countrystatecity.in/v1/countries/',
    apiUrLPart2: '/cities',
    apiKey: 'VUpsZ003Sk56T1E0UUNkUVVBSTEya01Id0c3dE5IejhNSGFKekFGNA=='
}
let cityList = [];


document.addEventListener('DOMContentLoaded', function() {

    // City dropdown thing was not part of the django form, so add it now
    addDropdown();


    // Load initial list of cities
    getCityList();

    // Changing the country creates a new list
    document.getElementById('country').addEventListener('change', () => getCityList());

    // Dynamic search for cities
    const cityInput = document.getElementById('city');
    cityInput.addEventListener("input", () => dynamicInputChange(cityInput));
})


//Function requests all cities of a country and turns them into a list
async function getCityList() {
    var newCountry = document.getElementById('country').value;
    let ApiURL = config.apiUrLPart1 + newCountry + config.apiUrLPart2;
    const data = await fetch(ApiURL, {headers: {"X-CSCAPI-KEY": config.apiKey}});
    const cities = await data.json();
    cityList = cities.map((city) => {
        return city.name;
    })
    delete cities;
    console.log(cityList);
}


// Creates the dropdown html element
function addDropdown() {
    const dropDown = document.createElement('div');
    dropDown.innerHTML = `
            <ul class="dropdown-autocomplete-list">
          <li>
            <button>Moscow</button>
          </li>
            <li>
            <button>Kazan</button>
          </li>
            <li>
            <button>Arkhangelsk</button>
          </li>
        </ul>
    `;
    var newCountry = document.getElementById('city');
    newCountry.after(dropDown);
}


function dynamicInputChange(cityInput) {
    const letters = cityInput.value.toLowerCase();
    console.log(letters);
}



