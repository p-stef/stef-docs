Permissions
===========

In **v2 of the React Showcase**, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam laoreet, erat eu auctor facilisis, felis mauris gravida felis, malesuada laoreet justo nulla et nunc. Mauris pharetra lectus vitae rutrum tincidunt. Quisque semper augue a quam venenatis sollicitudin. Quisque magna ex, auctor at sapien vel, auctor placerat enim. Aenean justo nunc, dictum nec nisl non, commodo elementum dui. Nam sem eros, molestie interdum egestas non, cursus nec metus. Morbi eleifend id ante at bibendum. Fusce accumsan tristique elit et mattis. Nulla ac varius purus, ac gravida dui. Duis ligula libero, mattis eu risus eu, faucibus ornare est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque sagittis accumsan arcu maximus cursus. Aliquam odio orci, iaculis eget placerat sit amet, varius eget felis. Aenean ut urna dapibus, laoreet massa a, sodales libero.

Setting Up Permissions
----------------------

Nullam auctor mi vitae libero accumsan, et porta justo vulputate. Pellentesque vitae neque non neque bibendum elementum. Curabitur ipsum justo, placerat sit amet auctor sit amet, ullamcorper vitae arcu. Nullam posuere quam vel dolor lobortis, at ultrices augue.

.. code-block:: javascript

    login() {
        let loginModel = {
            ...
        };
        
        UserApi.Login(loginModel)
            .then((user) => {
                setPermissions(user.permissions);
                // DO STUFF AND REDIRECT
            })
            .catch((errors) => {
                // HANDLE LOGIN ERRORS
            });
    }

