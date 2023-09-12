document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMloaded');

    // Use buttons to toggle between register options
  document.querySelector('#employer_register').addEventListener('click', () => load_register_form());

})


function load_register_form() {
    let reg_state = document.getElementById('register_label').innerHTML.substring(12);
    if (reg_state == 'a job seeker') {
    document.getElementById('employer_register').innerHTML = 'Switch to job seeker';
    document.getElementById('register_label').innerHTML = 'Register as an employer';
    } else if (reg_state == 'an employer') {
    document.getElementById('employer_register').innerHTML = 'Switch to employer';
    document.getElementById('register_label').innerHTML = 'Register as a job seeker';
    }
}