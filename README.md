A Django app has been created that implements a tree-like menu, adhering to the following conditions:

The menu is implemented through a template tag.
Everything above the highlighted item is expanded. The first level of nesting under the highlighted item is also expanded.
Stored in the database.
Edited in the standard Django admin.
The active menu item is determined based on the current page URL.
There can be several menus on one page. They are identified by name.
Clicking on a menu item navigates to the specified URL. The URL can be specified either explicitly or through a named URL.
Exactly one database query is required to render each menu.
A Django app is needed that allows menus (one or more) to be entered into the database through the admin, and to render a menu on any required page by name.
