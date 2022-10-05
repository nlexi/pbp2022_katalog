# Assignment 4 PBP/PBD

### CSRF Token
Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application. CRSF token is a unique value that is generated by server-side to protect CSRF vulnerable resources. If there's no {% csrf_token %}, the request will be rejected and the user session will be terminated thus the event will be identified as a CSRF attack.

### Creating Form Manually
Yes, we can create form element manually by not using .as_table altogether or using different commands such as forms.as_p or by using some outside help like bootstrap if we want to format it. By using those things we can customize the forms more freely and creatively. We can also create the form using the built in form in html but it will require more work.

### Data Flow Process
The flow of data from forms is first the user fills out the data, then it will be stored in the database model and it will be passed onto the html page. After that, it will be displayed for the user to see.

### Process of Completion
Step by step process:
- Create a new application named `todolist`
- Add `todolist` into project_django's settings and url
- Create user model using foreign key and also other models then makemigrations and migrate the model
- Implement login, register, and logout similar to lab 03
- Create button in `todolist.html` that redirects into `create-task.html`
- Create `forms.py` that contains the form that will be used
- Create new function in `views.py` that retrieves data from the form and redirects as soon as you submit the form
- Add, commit, and push the code onto GitHub then deploy the app on heroku
- Create two accounts with each having 3 tasks in the heroku app
- Answer assignment 4's question by updating `READ.ME`

[Heroku for Assignment 4](https://pbp2022-katalog.herokuapp.com/todolist)

# Assignment 5 PBP/PBD

### Diffrences
Inline CSS is styling used in the same line as the tag for example `<div style="color : black">`.
Internal CSS is styling inside the html file, but putting all the styling in a seperate tag called `<style>`. 
External CSS is styling done outside of the html file and calling it onto the html file.

### HTML Tags
There are many different tags in HTMl, these are some of them :
`<div>` general section in document
`<p>` paragraph/text
`<h1> to <h6>` headings
`<button` creates a button
`<table>, <tr>, <td>, <th>` creating a table, table row, table data, and table header respectively
`<img>` loads an image
`<form>` creates a form
`<input>` recieves input from the user based on the type chosen
`<title>` defines document title
`<li>, <ul>` defines a list and an unordered list respectively
`<a>` contains a hyperlink
`<nav>` defines navigation list
`<style>` contains style section for the document
`<body>` define document body
`<br>` create a single-line break

### CSS Selectors
`element` selects all elements of that kind
`.class` selects all classes that uses that name
`:hover` does something when hovering using mouse
`::after` inserting after content of element
`::before` inserting before content of element
`*` selects all elements

### Process of Completion
Step by step process:
- Import bootstrap into `base.html` in templates folder
- Customize the login, registration, and create-task page following bootstrap form docs 
- Customize `todolist.html` by adding a navbar, and changing task display into cards
- Add hover effect to the cards by using `:hover`
- Add, commit, and push the code onto GitHub
- Answer assignment 5's questions by updating `READ.ME`