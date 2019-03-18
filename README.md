# djangowebpack
Base project example to work with django react and webpack

## Command
**create_view**:
  params: view_name, title (optional)
  Command to create new base template to work with django y react
  
  **Example**: *python manage.py create_view my_view* will generate the respective folder in `assets/src/js/apps/my_view` with an entry point written in ReactJS and a template in `templates/frontend/test_view/index.html`
  Now you only need to create an url or a view to point to that template to use it, and thats it.
  
  You can run `npm run start` to update the bundles related to the react files where you are working on.
