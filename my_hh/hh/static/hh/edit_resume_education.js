   // Necessary global variables
var config = {
    eduCounter: 0,
}

// Main function starts after the DOM was loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');

    // Activate delete Xmark for existing blocks

    activateXmarks();

    // Education => add one more place of study
    document.getElementById('btn_study_add').addEventListener('click', () => AddNewStudyPlace(event));

});


function activateXmarks() {
    document.querySelectorAll('[id^="delete-"]').forEach((button) => {
       var x_id = button.id.split('-')[1];
       button.addEventListener('click', () => deleteStudyPlace(x_id));
    });
}


// Add one more empty place of study
function AddNewStudyPlace(event) {
    event.preventDefault();
    config.eduCounter += 1;

    var edu_id = Math.random().toString(16).slice(2);
    generateEducationBlockHtml(edu_id);
}


function generateEducationBlockHtml(edu_id) {
        var educationMainDiv = document.getElementById('resume_education_block');
    var newFormElement =  document.createElement('div');
    newFormElement.classList.add('education-block');
    newFormElement.setAttribute('id', `edu-element-${config.eduCounter}`)
    newFormElement.innerHTML = `
        <p>
        <div class="d-flex justify-content-between"><label for="educational_institution" class="form-label"> Educational institution: </label><a id="delete-${config.eduCounter}" class="delete-xmark"><i class="fa-solid fa-xmark fa-lg"></i></a></div>
        <input type="text" name="educational_institution:${edu_id}" class="form-control" maxlength="200" required="" id="educational_institution_${config.eduCounter}">
        </p>
        <p>
        <label for="specialization" class="form-label"> Specialization: </label>
        <input type="text" name="specialization:${edu_id}" class="form-control" maxlength="200" required="" id="specialization">
        </p>
        <p>
        <label for="year_of_graduation" class="form-label"> Year of graduation: </label>
        <input type="number" name="year_of_graduation:${edu_id}" class="form-control" required="" id="year_of_graduation">
        </p>
    `
    var deleteButton = newFormElement.querySelector('[id^="delete-"]');
    var selectedNum = config.eduCounter;
    deleteButton.addEventListener('click', () => deleteStudyPlace(selectedNum));
    educationMainDiv.append(newFormElement);
}


function deleteStudyPlace(selectedNum) {
    var studyPlaceId = 'edu-element-' + selectedNum;
    document.getElementById(studyPlaceId).remove();
}



function AddWorkPlace(event) {
    event.preventDefault();
    var previousJobMainDiv = document.getElementById('resume_previous_job_block');
    var newFormElement = document.createElement('div');
    newFormElement.innerHTML =
        `<p>
        <input type="hidden" name="secret_id" value="123">
        <label for="organization" class="form-label"> Organization: </label>
        <input type="text" name="organization" class="form-control" maxlength="200" required id="organization">
        </p>
        <p>
        <label for="industry" class="form-label"> Job function: </label>
        <input type="text" name="industry" class="form-control" maxlength="200" required id="industry">
        </p>
        <p>
        <label for="position" class="form-label"> Position: </label>
        <input type="text" name="position" class="form-control" maxlength="200" required id="position">
        </p>
    `
    previousJobMainDiv.append(newFormElement);
}