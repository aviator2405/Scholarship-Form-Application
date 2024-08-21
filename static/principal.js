
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function openApplicationForm(userID) {
    const apiURL = `http://127.0.0.1:8000/api/users/getFormPerInfo/${userID}/`;

    fetch(apiURL)
        .then(response => response.json())
        .then(data => {
            const personalInfo = data[0];
            const educationInfo = data[1];
            const bankDetails = data[2];
            const documentUrls = data[3];

            const newWindow = window.open('', '_blank', 'width=800,height=600');

            let htmlContent = `
                <html>
                <head>
                    <title>Application Form</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 20px; }
                        .section { margin-bottom: 20px; }
                        .section h2 { border-bottom: 2px solid #000; padding-bottom: 5px; }
                        .section p { margin: 5px 0; }
                        .section a { color: blue; text-decoration: underline; }
                    </style>
                </head>
                <body>
                    <h1>Application Form</h1>
                    
                    <div class="section">
                        <h2>Personal Information</h2>
                        <p><strong>Full Name:</strong> ${personalInfo.fullName}</p>
                        <p><strong>Date of Birth:</strong> ${personalInfo.dob}</p>
                        <p><strong>Gender:</strong> ${personalInfo.gender}</p>
                        <p><strong>Category:</strong> ${personalInfo.category}</p>
                        <p><strong>Caste Certificate No:</strong> ${personalInfo.caste_certi_no}</p>
                        <p><strong>Aadhar:</strong> ${personalInfo.aadhar}</p>
                        <p><strong>Father's Name:</strong> ${personalInfo.father}</p>
                        <p><strong>Phone:</strong> ${personalInfo.phone}</p>
                        <p><strong>Email:</strong> ${personalInfo.email}</p>
                        <p><strong>Income:</strong> ${personalInfo.income}</p>
                        <p><strong>Address:</strong> ${personalInfo.address}</p>
                        <p><strong>Pincode:</strong> ${personalInfo.pincode}</p>
                    </div>

                    <div class="section">
                        <h2>Education Information</h2>
                        <p><strong>Institution Name:</strong> ${educationInfo.InstName}</p>
                        <p><strong>Address:</strong> ${educationInfo.address}</p>
                        <p><strong>Enrollment:</strong> ${educationInfo.enrollment}</p>
                        <p><strong>Program:</strong> ${educationInfo.program}</p>
                        <p><strong>Current Year:</strong> ${educationInfo.year}</p>
                        <p><strong>Percentage/CGPA:</strong> ${educationInfo.percent}</p>
                        <p><strong>Passing Year:</strong> ${educationInfo.passingYear}</p>
                        <p><strong>Marksheet:</strong> <a href="${educationInfo.marksheet}" target="_blank">View Marksheet</a></p>
                    </div>

                    <div class="section">
                        <h2>Bank Details</h2>
                        <p><strong>Account Holder Name:</strong> ${bankDetails.accHolderName}</p>
                        <p><strong>Account Number:</strong> ${bankDetails.accNumber}</p>
                        <p><strong>Bank Name:</strong> ${bankDetails.bankName}</p>
                        <p><strong>Branch Name:</strong> ${bankDetails.branchName}</p>
                        <p><strong>IFSC Code:</strong> ${bankDetails.ifsc}</p>
                    </div>

                    <div class="section">
                        <h2>Document URLs</h2>
                        <p><strong>Caste Certificate:</strong> <a href="${documentUrls.casteCerti}" target="_blank">View Document</a></p>
                        <p><strong>Income Certificate:</strong> <a href="${documentUrls.incomeCerti}" target="_blank">View Document</a></p>
                        <p><strong>Aadhaar:</strong> <a href="${documentUrls.aadhaar}" target="_blank">View Document</a></p>
                        <p><strong>Photo:</strong> <a href="${documentUrls.photo}" target="_blank">View Photo</a></p>
                        <p><strong>Signature:</strong> <a href="${documentUrls.sign}" target="_blank">View Signature</a></p>
                        <p><strong>Admission Letter:</strong> <a href="${documentUrls.addmissionLetter}" target="_blank">View Letter</a></p>
                    </div>
                </body>
                </html>
            `;

            newWindow.document.write(htmlContent);
            newWindow.document.close();
        })
        .catch(error => console.error('Error fetching application data:', error));
}


fetch('http://127.0.0.1:8000/api/users/approvedByPRI/')
    .then(response => response.json())
    .then(approvedUsers => {
        const approvedUsernames = approvedUsers.map(user => user.username);

       
        return fetch('http://127.0.0.1:8000/api/users/approvedByHOD')
            .then(response => response.json())
            .then(usernames => {
                console.log(usernames);
                const filteredUsernames = usernames.filter(user => !approvedUsernames.includes(user.username));

                const promises = filteredUsernames.map(user => 
                    fetch(`http://127.0.0.1:8000/api/users/${user.username}`)
                        .then(response => response.json())
                );

                return Promise.all(promises);
            });
    })
    .then(usersData => {
        console.log(usersData);
        const combinedData = usersData.map(user => ({
            username: user[0].username,
            fullname: `${user[0].first_name} ${user[0].last_name}`,
            formLink: `javascript:openApplicationForm(${user[0].id})`, 
            userID: user[0].id 
        }));
        console.log(combinedData);
        populateUI(combinedData);
    })
    .catch(error => console.error('Error fetching data:', error));


function populateUI(apiData) {
    const container = document.getElementById('container'); 

    apiData.forEach(data => {
        // Create the main div
        const formHolder = document.createElement('div');
        formHolder.classList.add('form_holders');


        const leftSection = document.createElement('div');
        leftSection.classList.add('leftSection');

        const usernameSpan = document.createElement('span');
        usernameSpan.classList.add('sideHeading');
        usernameSpan.textContent = `Username: ${data.username}`;
        leftSection.appendChild(usernameSpan);
        leftSection.appendChild(document.createElement('br'));

        const fullnameSpan = document.createElement('span');
        fullnameSpan.classList.add('sideHeading');
        fullnameSpan.textContent = `Fullname: ${data.fullname}`;
        leftSection.appendChild(fullnameSpan);
        leftSection.appendChild(document.createElement('br'));

        const formLinkSpan = document.createElement('span');
        formLinkSpan.classList.add('sideHeading');
        formLinkSpan.innerHTML = `Application Form: <a class="linkToForm" href="${data.formLink}">Click to open Form</a>`;
        leftSection.appendChild(formLinkSpan);

        formHolder.appendChild(leftSection);


        const rightSection = document.createElement('div');
        rightSection.classList.add('rightSection');

        const acceptButton = document.createElement('button');
        acceptButton.type = 'button';
        acceptButton.id = "accBtn";
        acceptButton.classList.add('AccRejBtn');
        acceptButton.textContent = 'Accept';
        rightSection.appendChild(acceptButton);

        const rejectButton = document.createElement('button');
        rejectButton.type = 'button';
        rejectButton.classList.add('AccRejBtn');
        rejectButton.id = 'rejBtn';
        rejectButton.textContent = 'Reject';
        rightSection.appendChild(rejectButton);

        formHolder.appendChild(rightSection);

      
        container.appendChild(formHolder);


        rejectButton.addEventListener('click', function() {
         
            if (!formHolder.querySelector('.rejectForm')) {
          
                const rejectForm = document.createElement('form');
                rejectForm.classList.add('rejectForm');

                const inputField = document.createElement('input');
                inputField.type = 'text';
                inputField.placeholder = 'Reason for rejection';
                inputField.required = true;
                rejectForm.appendChild(inputField);

                const submitButton = document.createElement('button');
                submitButton.type = 'submit';
                submitButton.textContent = 'Submit';
                rejectForm.appendChild(submitButton);

           
                formHolder.appendChild(rejectForm);

         
                rejectForm.addEventListener('submit', function(event) {
                    event.preventDefault();

                    const reason = inputField.value;
                    useridnumber = data.userID
                  
                    alert(`Rejection reason submitted: ${reason}`);
                    const postData = {
                        username: data.userID, 
                        rejectMessage: reason 
                    };
                    console.log(postData);

                   
                    fetch('http://127.0.0.1:8000/api/users/prirejected/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')  
                        },
                        body: JSON.stringify(postData)
                    })
                    .then(response => {
                        if (response.ok) {
                 
                            return fetch(`http://127.0.0.1:8000/api/users/deleteFormPRI/${useridnumber}/`, {
                                method: 'DELETE',
                                headers: {
                                    'X-CSRFToken': getCookie('csrftoken')
                                }
                            });
                        }
                        throw new Error('Network response was not ok.');
                    })
                    .then(() => {
                        console.log('Form deleted after rejection');
                        rightSection.innerHTML = '<span class="statusText rejected" style="color: red;">Rejected</span>';
                    })
                    .catch(error => {
                        console.error('Error during rejection:', error);
                        alert('Failed to reject the application.');
                    });
                    rejectForm.remove();
                    
                    rightSection.innerHTML = '<span class="statusText rejected" style="color: red;">Rejected</span>';
                });
            }
        });

        
        acceptButton.addEventListener('click', function() {
           
            alert('Application accepted');
            const postData = {
                username: data.userID, 
            };
            console.log(postData);
            
            fetch('http://127.0.0.1:8000/api/users/priapproved/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  
                },
                body: JSON.stringify(postData)
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then(data => {
                console.log('Server response:', data);
                rightSection.innerHTML = '<span class="statusText accepted">Accepted</span>';
            })
            .catch(error => {
                console.error('Error during acceptance:', error);
                alert('Failed to accept the application.');
            });

         
            rightSection.innerHTML = '<span class="statusText accepted">Accepted</span>';
        });
    });
}
