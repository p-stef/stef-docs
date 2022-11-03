Input
=====

Rather than using a standard input via HTML, you should always use a **React Showcase Input**. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam laoreet, erat eu auctor facilisis, felis mauris gravida felis, malesuada laoreet justo nulla et nunc.

The Default Input
-----------------

Mauris pharetra lectus vitae rutrum tincidunt. Quisque semper augue a quam venenatis sollicitudin. Quisque magna ex, auctor at sapien vel, auctor placerat enim.

.. code-block:: javascript

    <Input
        name="myInput"
        onChange={(e) => this.setState({ inputValue: e.currentTarget.value })}
        value={this.state.inputValue ?? ""}
    />


The Number Input Example
------------------------

Aenean justo nunc, dictum nec nisl non, commodo elementum dui. Nam sem eros, molestie interdum egestas non, cursus nec metus. Morbi eleifend id ante at bibendum.

.. code-block:: javascript
    
    render() {
        return (
            <Input
                name="myNumberInput"
                min={-10}
                max={1000}
                step={1}
                type="number"
                className="myCustomClass"
                onChange={(e) => this.handleNumberInputChanged(e)}
                value={this.state.numberInputValue ?? ""}
            />
        );   
    }

    handleNumberInputChanged(e: React.ChangeEvent<HTMLInputElement>) {
        ...
    }


