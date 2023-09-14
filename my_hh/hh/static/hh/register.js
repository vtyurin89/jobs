document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMloaded');

    // Use buttons to toggle between register options
  load_job_seeker_form();
  document.querySelector('#employer_register').addEventListener('click', () => load_register_form());

})

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
        <select class="form-select mt-1" id="gender-select" name='gender'>
          <option selected value="P">Gender</option>
          <option value="M">Male</option>
          <option value="F">Female</option>
          <option value="U">Unspecified</option>
        </select>
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