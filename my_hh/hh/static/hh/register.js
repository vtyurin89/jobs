// Necessary global variables
var config = {
    apiUrLPart1: 'https://api.countrystatecity.in/v1/countries/',
    apiUrLPart2: '/cities',
    apiKey: 'VUpsZ003Sk56T1E0UUNkUVVBSTEya01Id0c3dE5IejhNSGFKekFGNA==',
    cityList: [],
}


document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMloaded');

    // Use buttons to toggle between register options
    load_job_seeker_form();
    document.querySelector('#employer_register').addEventListener('click', () => load_register_form());

    addDropdown();

    // Changing the country creates a new list
    const cityInput = document.getElementById('city');
    document.getElementById('country').addEventListener('change', () => getCityList());

    // Dynamic search for cities
    cityInput.addEventListener("input", () => dynamicInputChange(cityInput));
})


//Function requests all cities of a country and turns them into a list of names
async function getCityList() {
    const inputCity = document.getElementById('city');
    inputCity.value = "";

    var newCountry = document.getElementById('country').value;
    if (newCountry == "None") {
        inputCity.disabled = true;
    } else {
        inputCity.disabled = false;
        let ApiURL = config.apiUrLPart1 + newCountry + config.apiUrLPart2;
        const data = await fetch(ApiURL, {headers: {"X-CSCAPI-KEY": config.apiKey}});
        const citiesJson = await data.json();
        config.cityList = citiesJson.map((city) => {
        return city.name;
    })
    delete citiesJson;
    console.log(config.cityList);
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


//toggle between two register forms
function load_register_form() {
    let reg_state = document.getElementById('register_label').innerHTML.substring(12);
    if (reg_state == 'a job seeker') {
    document.getElementById('employer_register').innerHTML = 'Switch to job seeker';
    document.getElementById('register_label').innerHTML = 'Register as an employer';
    load_employer_form();


    } else if (reg_state == 'an employer') {
    document.getElementById('employer_register').innerHTML = 'Switch to employer';
    document.getElementById('register_label').innerHTML = 'Register as a job seeker';
   load_job_seeker_form();
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

















// Checks if registration form is valid
function form_validation () {
  var form = document.getElementById('reg_form_main');

  form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
      }, false)
}


//loads job seeker form html
function load_job_seeker_form(){
    document.getElementById('reg_form_main').innerHTML = `
            <input type="hidden" name="user_type" value="job_seeker"/>
            <div class="form-group mt-3">
            <input class="form-control" autofocus type="text" name="username" placeholder="Username *" required>
            <input class="form-control mt-1" type="email" name="email" placeholder="Email Address *" required>
            <input class="form-control mt-1" type="password" name="password" placeholder="Password *" required>
            <input class="form-control mt-1" type="password" name="confirmation" placeholder="Confirm Password *" required>
        </div>

        <div class="form-group mt-5">
            <label for="first_name" class="form-label">Personal information</label>
            <input class="form-control mt-1" type="text" name="first_name" id="first_name" placeholder="First Name *" required>
            <input class="form-control mt-1" type="text" name="last_name" placeholder="Last Name *" required>
        </div>

        <div class="form-group mt-5">
            <label for="country" class="form-label">Location</label>
            <select class="form-select" aria-label="Select country" name="country" id="country">
              <option selected value="None">Country</option>
              <option value="RU">Russia</option>
              <option value="KZ">Kazakhstan</option>
              <option value="BY">Belarus</option>
              <option value="UZ">Uzbekistan</option>
              <option value="AZ">Azerbaijan</option>
              <option value="GE">Georgia</option>
              <option value="KG">Kyrgyzstan</option>
            </select>
            <input class="form-control mt-1" type="text" name="city" id="city" placeholder="City" disabled>
        </div>

        <div class="form-group mt-5">
            <label for="phone-number" class="form-label">Contacts</label>
            <input class="form-control mt-1" type="text" id="phone-number" name="phone_number" placeholder="Phone number">
            <input class="form-control mt-1" type="text" name="telegram_ID" placeholder="Telegram ID">
        </div>

        <div class="form-group mt-5">
            <label for="photo" class="form-label">Photo</label>
            <input class="form-control mt-1" type="url" id="photo" name="photo" placeholder="Photo URL">
        </div>

        <div class="d-flex justify-content-center"><input class="btn btn-primary mt-3" type="submit" value="Register"></div>
        </div>
    `;
}

//loads employer form html
function load_employer_form() {
    document.getElementById('reg_form_main').innerHTML = `
            <input type="hidden" name="user_type" value="employer"/>
            <div class="form-group mt-3">
            <input class="form-control" autofocus type="text" name="username" placeholder="Username *" required>
            <input class="form-control mt-1" type="email" name="email" placeholder="Email Address *" required>
            <input class="form-control mt-1" type="password" name="password" placeholder="Password *" required>
            <input class="form-control mt-1" type="password" name="confirmation" placeholder="Confirm Password *" required>
        </div>

        <div class="form-group mt-5">
            <label for="first_name" class="form-label">Your company (if any)</label>
            <input class="form-control mt-1" type="text" name="company_name" id="company_name" placeholder="Company name *" required>
            <input class="form-control mt-1" type="url" id="company_logo" name="company_logo" placeholder="Company logo URL">
        </div>

        <div class="form-group mt-5">
            <label for="first_name" class="form-label">Personal information</label>
            <input class="form-control mt-1" type="text" name="first_name" id="first_name" placeholder="First Name *" required>
            <input class="form-control mt-1" type="text" name="last_name" placeholder="Last Name *" required>
        </div>


        <div class="form-group mt-5">
            <label for="phone-number" class="form-label">Contacts</label>
            <input class="form-control mt-1" type="text" id="phone-number" name="phone_number" placeholder="Phone number">
            <input class="form-control mt-1" type="text" name="telegram_ID" placeholder="Telegram ID">
        </div>

        <div class="d-flex justify-content-center"><input class="btn btn-primary mt-3" type="submit" value="Register"></div>
        </div>
    `;
}