   // Necessary global variables
var config = {
    eduCounter: 0,
}

// Main function starts after the DOM was loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');


    // Education => add one more place of study
    document.getElementById('btn_study_add').addEventListener('click', () => AddStudyPlace(event));

    // Work experience => add one more previous job
    document.getElementById('btn_employer_add').addEventListener('click', () => AddWorkPlace(event));

});


// Add one more place of study
function AddStudyPlace(event) {
    event.preventDefault();
    config.eduCounter += 1;

    var educationMainDiv = document.getElementById('resume_education_block');
    var newFormElement =  document.createElement('div');
    newFormElement.classList.add('education-block');
    newFormElement.setAttribute('id', `edu-element-${config.eduCounter}`)
    newFormElement.innerHTML = `
        <p>
        <div class="d-flex justify-content-between"><label for="educational_institution" class="form-label"> Educational institution: </label><a id="delete-${config.eduCounter}"><i class="fa-solid fa-xmark fa-lg"></i></a></div>
        <input type="text" name="educational_institution" class="form-control" maxlength="200" required="" id="educational_institution">
        </p>
        <p>
        <label for="specialization" class="form-label"> Specialization: </label>
        <input type="text" name="specialization" class="form-control" maxlength="200" required="" id="specialization">
        </p>
        <p>
        <label for="year_of_graduation" class="form-label"> Year of graduation: </label>
        <input type="date" name="year_of_graduation" class="form-control" required="" id="year_of_graduation">
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
    console.log(`Removed element ${selectedNum}`)
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