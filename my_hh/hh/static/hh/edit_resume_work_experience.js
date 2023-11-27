

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');

    // Activate delete Xmark for existing blocks

    activateXmarks();

    // Education => add one more place of study
    document.getElementById('btn_employer_add').addEventListener('click', () => AddNewWorkPlace(event));


});


function activateXmarks() {
    document.querySelectorAll('[id^="delete-"]').forEach((button) => {
       var x_id = button.id.split('-')[1];
       button.addEventListener('click', () => deleteWorkPlace(x_id));
    });
}


function AddNewWorkPlace(event) {
    event.preventDefault();
    var work_id = Math.random().toString(16).slice(2);

    generateWorkPlaceBlockHtml(work_id);
}


function generateWorkPlaceBlockHtml(work_id) {
    var previousJobMainDiv = document.getElementById('resume_previous_job_block');
    var newFormElement = document.createElement('div');
    newFormElement.classList.add('education-block');
    newFormElement.setAttribute('id', `work-element-${work_id}`)

    newFormElement.innerHTML =
        `<p>
        <div class="d-flex justify-content-between"><label for="organization" class="form-label"> Organization: </label><a id="delete-${work_id}" class="delete-xmark"><i class="fa-solid fa-xmark fa-lg"></i></a></div>
        <input type="text" name="organization:${work_id}" class="form-control" maxlength="200" required id="organization">
        </p>
        <p>
        <label for="position" class="form-label"> Position: </label>
        <input type="text" name="position:${work_id}" class="form-control" maxlength="200" required id="position">
        </p>
        <p>
        <label for="job_duties" class="form-label"> Job duties: </label>
        <textarea rows="3" maxlength="1500" name="job_duties:${work_id}" class="form-control" required id="job_duties"></textarea>
        </p>
        <p>
        <label for="employment_began" class="form-label"> Was employed since: </label>
        <input type="month" min="1900-01" name="employment_began:${work_id}" class="form-control" maxlength="200" required id="employment_began">
        </p>
        <p>
        <label for="employment_ended" class="form-label"> Was employed until: </label>
        <input type="month" min="1900-01" name="employment_ended:${work_id}" class="form-control" maxlength="200" id="employment_ended">
        </p>
        `

    var deleteButton = newFormElement.querySelector('[id^="delete-"]');
    deleteButton.addEventListener('click', () => deleteWorkPlace(work_id));
    previousJobMainDiv.append(newFormElement);
}

function deleteWorkPlace(work_id) {
    var workPlaceId = 'work-element-' + work_id;
    document.getElementById(workPlaceId).remove();
}