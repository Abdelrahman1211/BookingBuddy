# README.md

## Introduction

Welcome to the Booking Website! This web application is designed to showcase our team's project. It includes various features and functionalities implemented using HTML, CSS, Bootstrap, Flask, Jinja, JSON, JavaScript, and jQuery. The website provides a convenient platform for users to book hotels, flights, cars, and more. With a user-friendly interface and a range of features, we aim to make the booking process seamless and enjoyable.


## How to Run the Web Application

To run the web application locally, follow these steps:

1. Clone the project repository from GitHub.
2. Set up a virtual environment using the `venv` folder provided.
3. Install the required dependencies listed in the `requirements.txt` file.
4. Run the Flask application using the command `flask run`.
5. Access the web application in your browser using the provided URL.

## Team Members

The team members involved in this project are:

- Abdelrahman EL-Sayed ([GitHub](https://github.com/Abdelrahman1211))
- Sultan Bakhsh ([GitHub](https://github.com/5ultan22))

## Structure and Design

The project files are organized as follows:

- `static/`: Contains the CSS file (`style.css`) and any other static assets.
- `templates/`: Contains the HTML templates for different pages.
- `data/`: Contains the JSON data file (`mobile-data.js`) used in the application.
- `app.py`: The main Flask application file.
- `postsdata.py`: Contains data retrieval functions using Jinja.
- `README.md`: This file.
- `CONTRIBUTORS.md`: Lists all the contributors to the project.

## Main Menu

The main menu, designed as a navigation bar using Bootstrap, appears at the top of all pages. It includes links to different sections of the website, allowing easy navigation for users.

## CSS Styling

The CSS file (`style.css`) is included and linked to all pages, providing consistent styling and layout across the entire website.

## Contact Us Form

The "Contact Us" form includes a message textbox and a submit button. When submitted, the form data is sent to the official email of the website for further processing.

## Images

All images used in the website are displayed using fake images generated by [https://fakeimg.pl/](https://fakeimg.pl/). The images are resized to fit the desired dimensions within the web pages.

## Font Awesome Icons

The website utilizes Font Awesome icons by linking to [https://fontawesome.com](https://fontawesome.com). A minimum of 5 icons are used throughout the website to enhance the visual presentation and user experience.

## JSON Data

The `mobile-data.js` file contains a JSON object that holds a list of objects representing mobile data. This data is used to populate the mobiles.html page dynamically using JavaScript and Bootstrap elements.

## jQuery AJAX

The website incorporates jQuery AJAX to request and present data from the `mobile-data.js` file into an HTML container on the `reqres-data.html` page. The data is dynamically generated using JavaScript.

## Flask Integration

Flask is used to handle page requests and provide server-side functionality. The layout is applied to all pages through the use of templates. The Jinja templating engine is used to bring data from `postsdata.py` into the `post-all.html` page and to make parametrized requests. The `app.py` file handles routing and sends emails using Flask's email functionality.

## Postman Integration

Postman is utilized for various purposes, including creating a team workspace, inviting team members, and testing API requests. The instructor, Sami AlFattani (sami_alfattani@hotmail.com), has been included as a collaborator in the Postman team workspace.

## Backend Testing

Various test cases on [https://reqres.in/](https://reqres.in/) have been performed using Postman. Each test case has been tested using code implementation after receiving the response. At least 2 test codes have been written for each test case to ensure accurate and robust backend functionality.

## Deployment

The web application is deployed using the Heroku platform. The project includes all necessary files, such as `requirements.txt`, `runtime.txt`, and `Procfile`, to ensure smooth deployment. The collaboration feature in Heroku is utilized to add all team members and the instructor, Wael Alghamdi (w.alghamdi@ubt.edu.sa), as collaborators in the Heroku app.

## Code Comments and File Organization

All code files are thoroughly commented to provide clear explanations and improve code readability. The project files are organized into appropriate folders to ensure a clean and structured project structure. All files are named using lowercase letters to maintain consistency and ease of access.

## Virtual Environment

A virtual environment folder named `venv` is included in the project. This folder is added to the `.gitignore` file to prevent it from being pushed to the repository. It is recommended to set up the virtual environment using the provided folder to isolate the project's dependencies.

Please refer to the project documentation and code files for more detailed information and instructions.
