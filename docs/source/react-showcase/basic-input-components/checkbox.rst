Checkbox
========

In **v2 of the React Showcase**, The checkbox component is a tri-state checkbox that is easily converted into a standard checkbox. Some examples are provided below.

.. warning::
    **Lorem ipsum dolor sit amet, consectetur adipiscing elit.**
    Nullam ut lorem sapien. In vehicula felis vitae finibus vestibulum. Mauris id nisl vehicula, egestas metus nec, interdum ligula

Dual-state Checkbox
-------------------

.. code-block:: javascript

    <Checkbox
        checked={this.state.checkValue}
        onChange={() => this.setState({ checkValue: !this.state.checkValue })}
    />


Tri-state Checkbox
-------------------

.. code-block:: javascript

    render() {
        return (
            <Checkbox
                checked={this.state.checkValue}
                onChange={() => this.handleNullStateCheckboxChanged()}
            />
        );
    }

    handleNullStateCheckboxChanged() {
        ...
    }
