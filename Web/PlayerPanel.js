class PlayerPanel extends React.Component {
    render() {
        return ('div', null, 'hello world');
    }
}

ReactDOM.render(
    React.createElement(PlayerPanel),
    document.querySelector('#PlayerPanel')
);