import React from 'react';

class HelloButton extends React.Component {
  handleClick = () => {
    alert('Hello!');
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        Hello
      </button>
    );
  }
}

export default HelloButton;
