Controller
==========

Controllers are saved in the **Controller** table.

Services: 

* **IControllerService** 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ex diam, venenatis vitae tristique a, eleifend et diam. Pellentesque laoreet dignissim sapien vitae commodo. Cras leo magna, bibendum gravida nunc at, ornare imperdiet dolor. 

Maecenas congue ultrices leo ac sollicitudin. Maecenas eu efficitur tellus:

* DefaultPermission: grants permissions to a specific controller
* OrganisationPermission: grants permissions to a specific organisation
* GroupPermission: grants permissions to a specific group 
* UserPermission: grants permissions to a specific user 

Quisque malesuada elementum lacus vitae vehicula. Nullam aliquet feugiat purus sed congue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus:

* Quisque malesuada elementum lacus vitae vehicula 
* Nullam aliquet feugiat purus sed congue. (Curabitur rutrum cursus lacus. Nulla ipsum enim, posuere sed varius non, pellentesque in sem. Aenean quis convallis libero.)

.. warning::
    Quisque malesuada elementum lacus vitae vehicula. Nullam aliquet feugiat purus sed congue. Orci varius natoque penatibus **pControllerAdd** magnis dis parturient montes, nascetur ridiculus mus. Curabitur rutrum cursus lacus. Nulla ipsum enim, posuere sed varius non, pellentesque in sem.

Here's few examples of how we can decorate routes inside a controller with specific permission levels: 

.. code-block:: csharp

    // Action only accessible if Read permissions are granted 
    [ReqPermission(Permission.Read)] 
    public IActionResult Get(int userID)


.. code-block:: csharp

    // Action only accessible if Add & Edit permissions are granted 
    [ReqPermission(Permission.Add & Permission.Edit)] 
    public IActionResult Save([FromBody] User user)


.. code-block:: csharp

    // Action only accessible if Delete permissions are granted 
    [ReqPermission(Permission.Delete)] 
    public IActionResult Delete(int userID)


Every controller in the back-end must be injected with the **IControllerService**, which will take care of some standard functionality, i.e. cache the conID for auditing purposes, etc.

Here's an example of a back-end controller constructor, with injection of **IControllerService**: 


.. code-block:: csharp

    public BookController(IHttpContextAccessor httpContextAccessor,
                           ILockService lockService,
                           IControllerService controllerService)
    : base(httpContextAccessor, lockService, controllerService)
    {
        //...
    }